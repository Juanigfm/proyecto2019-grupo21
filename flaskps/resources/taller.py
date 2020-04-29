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
from flaskps.models.taller import Taller
from flaskps.models.ciclos import Ciclo
from flaskps.models.clase import Clase
from flaskps.resources import ciclos
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
from flaskps.models.nucleo import Nucleo
import transaction
import re

def listado_talleres(params = { "init" : 0 }, function=1, activo = None, nombre = ''):
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
    if not usuarioTienePermiso("LISTADO_TALLERES"):
        return redirect(url_for('pages_home'))

    
    Pages.db = get_db()
    paginado = Pages.get_paginado()
    params['pag'] = int(paginado['cuerpo'])

    if request.method == 'POST' and 'init' in request.form.keys() and int(request.form['init'])>=0:
        params ['init'] = int(request.form['init'])

    filtro=''

    if ('nombreFiltro' in request.form.keys()):
        if (request.form['nombreFiltro'] and request.form['nombreFiltro'].strip()):
            nombre = request.form['nombreFiltro']
            function=0
            filtro=request.form['nombreFiltro']

    Taller.db = get_db()
    users = Taller.listado(nombre)

    return render_template('user/listadoTalleres.html', users=users, params=params, nombreFiltro=nombre, function=function, filtro=filtro)

def tallerCreatetTemp():
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
    Nucleo.db = get_db()
    nucleos = Nucleo.all()
    docentes = Docente.all()
    Ciclo.db = get_db()
    ciclos = Ciclo.all()

    return render_template('user/createTaller.html', docentes=docentes, ciclos=ciclos, mapeo=mapeo, nucleos=nucleos)

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
    if not usuarioTienePermiso("CREAR_TALLER"):
        return redirect(url_for('pages_home'))

    Taller.db = get_db()

    res = Taller.create(request.form['nombre'],request.form['nombrecorto'], request.form['nucleo'])
    Taller.assign_ciclo(res['idInsertado'],request.form['ciclo'])
    if request.form['docente'] != "0":
        Taller.assign_docente(request.form['docente'],res['idInsertado'])
    
    Taller.db.commit()
    
    flash("El taller ha sido creado correctamente.","success")
    if ('clid' in request.form.keys()):
        return ciclos.detalle()
    return redirect(url_for('listado_talleres'))

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
    if not usuarioTienePermiso("DETALLE_TALLER"):
        return redirect(url_for('pages_home'))

    Taller.db = get_db()
    Clase.db = get_db()
    taller = Taller.get_detalle_taller(request.form['id'])
    alumnos = Taller.get_alumnos_taller(request.form['id'])
    docentes = Taller.get_docentes_taller(request.form['id'])
    clases = Clase.get_clases_by_taller(request.form['id'])
    mapeo = request.form['mapeo']
    clid = request.form['clid']
    Estudiante.db = get_db()
    Docente.db = get_db()
    alums = Estudiante.entaller_no_rep(request.form['id'])
    docs = Docente.entaller_no_rep(request.form['id'])
    return render_template('user/detalleTaller.html', taller=taller, alumnos=alumnos, docentes=docentes, docs=docs, alums=alums, clid=clid, mapeo=mapeo, clases=clases)

def agregar_docente():
    Taller.db = get_db()
    Taller.assign_docente(request.form['docente'],request.form['id'])
    Taller.db.commit()
    flash("El docente ha sido agregado correctamente.","success")
    return detalle()

def agregar_alumno():
    Taller.db = get_db()
    Taller.assign_alumno(request.form['alumno'],request.form['id'])
    flash("El alumno ha sido agregado correctamente.","success")
    return detalle()

def baja_alumno():
    Taller.db = get_db()
    Taller.baja_alumno(request.form['alid'],request.form['id'])
    flash("El alumno ha sido removido correctamente.","success")
    return detalle()

def baja_docente():
    Taller.db = get_db()
    Clase.db = get_db()
    res = Clase.get_clases_by_docente_taller(request.form['docid'],request.form['id'])

    if res['cantidadClases'] == 0:
        Taller.baja_docente(request.form['docid'],request.form['id'])
        flash("El docente ha sido removido correctamente.","success")
    else:
        flash("El docente tiene clases asignadas y no puede removerse.","danger")
    return detalle()