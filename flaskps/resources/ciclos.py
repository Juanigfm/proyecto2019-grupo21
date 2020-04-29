from flask import redirect, flash, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers.auth import authenticated
from flaskps.forms import CreateUserForm
from wtforms import ValidationError
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.models.estudiantes import Estudiante
from flaskps.models.docentes import Docente
from flaskps.models.clase import Clase
from flaskps.models.taller import Taller
from flaskps.models.ciclos import Ciclo
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
from flaskps.models.nucleo import Nucleo
import transaction
import re


def listado_ciclos(params = { "init" : 0 }, function=1, activo = None, nombre = ''):
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
    if not usuarioTienePermiso("LISTADO_CICLOS"):
        return redirect(url_for('pages_home'))

    
    Pages.db = get_db()
    paginado = Pages.get_paginado()
    params['pag'] = int(paginado['cuerpo'])

    if request.method == 'POST' and 'init' in request.form.keys() and int(request.form['init'])>=0:
        params ['init'] = int(request.form['init'])

    Ciclo.db = get_db()
    users = Ciclo.all()

    return render_template('user/listadoCiclosLectivos.html', users=users, params=params, function=function)

def cicloCreatetTemp():
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
    if not usuarioTienePermiso("CREAR_CICLO"):
        return redirect(url_for('pages_home'))

    return render_template('user/createCiclo.html')

def create():
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
    if not usuarioTienePermiso("CREAR_CICLO"):
        return redirect(url_for('pages_home'))

    Ciclo.db = get_db()
    Ciclo.create(request.form['fecha_ini'], request.form['fecha_fin'], request.form['semestre'])
    flash("El ciclo ha sido creado correctamente.","success")
    return redirect(url_for('listado_ciclos'))
    
def detalle():
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
    if not usuarioTienePermiso("DETALLE_CICLO"):
        return redirect(url_for('pages_home'))

    Ciclo.db = get_db()
    ciclo = Ciclo.find_by_id(request.form['clid'])
    talleres = Ciclo.get_talleres(request.form['clid']) 
    # todost = Ciclo.get_talleres_sin_repeticion(request.form['clid'])
    return render_template('user/detalleCiclo.html', talleres=talleres, ciclo=ciclo)

def createTaller():
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
    if not usuarioTienePermiso("CREAR_TALLER"):
        return redirect(url_for('pages_home'))
    # if not authenticated(session):
    #     return render_template('auth/login.html')
    # ok=True
    # if not pageState():
    #     ok=False
    #     for permiso in session['permisos']:
    #         if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
    #             ok=True
    # if not ok:    
    #     return render_template('error/mantenimiento.html')
    # if not usuarioTienePermiso("CREAR_USUARIO"):
    #     return redirect(url_for('pages_home'))
    mapeo=request.form['mapeo']
    Docente.db = get_db()
    docentes = Docente.all()
    Ciclo.db = get_db()
    ciclos = Ciclo.all()
    Nucleo.db = get_db()
    nucleos = Nucleo.all()

    return render_template('user/createTaller.html', docentes=docentes, ciclos=ciclos, clid=request.form['clid'], mapeo=mapeo, nucleos=nucleos)

def delete():
    Ciclo.db = get_db()
    Taller.db = get_db()
    Clase.db = get_db()
    Ciclo.db.autocommit = False
    Taller.db.autocommit = False
    #obtengo los talleres del cliclo
    talleresDelCiclo = Ciclo.get_talleres(request.form['hiddenEmailD'])
    #solo borro el ciclo si no tiene talleres 
    # if (len(talleresDelCiclo) == 0):

    #ELIMINO TODAS LAS ASIGNACIONES DE TALLERES AL CICLO
    Ciclo.delete_clt(request.form['hiddenEmailD'])

    #ELIMINO LA ASIGNACIÓN DE ALUMNOS Y DOCENTES EN TALLERES ASOCIADOS AL CICLO
    for t in talleresDelCiclo:
        Taller.baja_alumnos(t['id'])
        Taller.baja_docentes(t['id'])
        Clase.desasignar(t['id'])
        Taller.delete(t['id'])
    
    #ELIMINO EL CICLO
    Ciclo.delete(request.form['hiddenEmailD'])

    Ciclo.db.commit()
    Taller.db.commit()
    flash("El ciclo ha sido borrado correctamente.","success")
    # else:
    #     flash("El ciclo no puede ser borrado, asegúrese de que no tenga talleres asignados.","danger")
    return redirect(url_for('listado_ciclos'))

def updateTemp():
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
    if not usuarioTienePermiso("MODIFICAR_CICLO"):
        return redirect(url_for('pages_home'))

    Ciclo.db = get_db()
    ciclo = Ciclo.find_by_id(request.form['clid'])
    return render_template('user/createCiclo.html', ciclo=ciclo)

def update():
    fechaInicio=request.form['fecha_ini']
    fechaFin=request.form['fecha_fin']
    if(fechaInicio > fechaFin):
        flash("La fecha inicio no puede ser mayor que la fecha fin","error")
    else:
        Ciclo.db = get_db()
        ciclo = Ciclo.update(request.form['fecha_ini'], request.form['fecha_fin'], request.form['semestre'], request.form['id'])
        flash("El ciclo ha sido modificado correctamente.","success")
        return redirect(url_for('listado_ciclos'))