from flask import redirect, flash, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.helpers.auth import authenticated, checkAccess
from flaskps.forms import CreateUserForm
from wtforms import ValidationError
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.models.estudiantes import Estudiante
from flaskps.models.clase import Clase
from flaskps.models.asistencia import Asistencia
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
from flaskps.models.asistencia import Asistencia
from flaskps.resources import taller
import transaction
import re


def tomarAsistenciaTemp():

    if not authenticated(session):
        return render_template('auth/login.html')
    ok=True
    if not pageState():
        ok=False
        for permiso in session['permisos']:
            if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
                ok=True
    if not ok:
        return render_template('error/mantenimiento.html')
    if not usuarioTienePermiso("CREAR_ASISTENCIA"):
        return redirect(url_for('pages_home'))

    tallerId = request.form['tallerId']
    clid = request.form['clid']
    mapeo = request.form['mapeo']

    #obtengo todas las clases asociadas a un taller
    Clase.db = get_db()
    clases = Clase.get_clases_by_taller(tallerId)

    #obtengo todos los estudiantes asociados al taller
    Estudiante.db = get_db()
    estudiantes = Estudiante.estudiantes_by_taller(tallerId)

    return render_template('user/listadoTomarAsistencia.html', clases=clases, alumnos=estudiantes, tallerId = tallerId, clid=clid, mapeo=mapeo)


def registrarAsistencias():

    if not authenticated(session):
        return render_template('auth/login.html')
    ok=True
    if not pageState():
        ok=False
        for permiso in session['permisos']:
            if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
                ok=True
    if not ok:
        return render_template('error/mantenimiento.html')
    if not usuarioTienePermiso("CREAR_ASISTENCIA"):
        return redirect(url_for('pages_home'))

    try:
        Asistencia.db = get_db()

        r = Asistencia.get_registro_by_clase_fecha(request.form['clase'],request.form['fecha'])
        if len(r) > 0:
            flash("La clase seleccionada ya tiene asistencias registradas", "danger")
            return tomarAsistenciaTemp()
        #obtengo todos los estudiantes asociados al taller
        Estudiante.db = get_db()
        estudiantes = Estudiante.estudiantes_by_taller(request.form['tallerId'])

        for e in estudiantes:
            nombreInput= 'presente'+ str(e['id'])
            valor = nombreInput in request.form
            Asistencia.insert_asistencia_de_estudiante(valor, e['id'], request.form['clase'], e['apellido'], e['nombre'], e['numero'], request.form['fecha']) 

        Asistencia.insert_asistencias_log(request.form['fecha'],request.form['clase'])

        Asistencia.db.commit()

        flash("Las asistencias se registraron con éxtio","success")
        #redireccionar al detalle de taller
        return taller.detalle()

    except Exception as e:
        Asistencia.db.rollback()
        flash(str(e), "danger")
        return taller.detalle()

def verAsistencias():

    if not authenticated(session):
        return render_template('auth/login.html')
    ok=True
    if not pageState():
        ok=False
        for permiso in session['permisos']:
            if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
                ok=True
    if not ok:
        return render_template('error/mantenimiento.html')
    if not usuarioTienePermiso("VER_ASISTENCIAS"):
        return redirect(url_for('pages_home'))
        
    Clase.db = get_db()
    mapeo = request.form['mapeo']
    if('tallerId' in request.form.keys()):    
        clases = Clase.get_clases_de_taller(request.form['tallerId'])   
        return render_template('user/verAsistencias.html', clases=clases, mapeo=mapeo, tallerId=request.form['tallerId'], clid=request.form['clid'])
    else:
        clases = Clase.get_clases_de_taller(request.form['idtaller'])
        log = Clase.get_log_by_id(request.form['idlog'])
        Asistencia.db = get_db()
        asistencias = Asistencia.get_asistencia_by_fecha_y_clase(log['clase_id'], log['fecha'])
        claseSeleccionada = request.form['idlog']
        return render_template('user/verAsistencias.html', claseSeleccionada = claseSeleccionada, asistencias=asistencias, clases=clases, funcion=0, mapeo=mapeo, tallerId=request.form['idtaller'], clid=request.form['clid'])