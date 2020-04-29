from flask import redirect, flash, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.helpers.auth import authenticated, checkAccess
from flaskps.forms import CreateUserForm
from wtforms import ValidationError
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.models.estudiantes import Estudiante
from flaskps.models.barrio import Barrio
from flaskps.models.genero import Genero
from flaskps.models.responsable import Responsable
from flaskps.models.escuela import Escuela
from flaskps.models.nivel import Nivel
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
import transaction
import re


def listadoAlumnos(params = { "init" : 0 }, function=1, activo = None, nombre = ''):
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
    if not usuarioTienePermiso("LISTADO_ALUMNOS"):
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
    #   MODIFICADO PARA USUARIO PERO HAYQ UE AGREGAR LOS FILTROS PARA LA BUSQUEDA
    Estudiante.db = get_db()
    users = Estudiante.get_listado(nombre)

    return render_template('user/listadoAlumnos.html', users=users, params=params, nombreFiltro=nombre, function=function, filtro=filtro)

def alumnoCreateTemp():
    resp = checkAccess("CREAR_ALUMNO")
    if resp=='true':
        return redirectCreateAlumno()
    else:
        return resp

def alumnoUpdateTemp():
    resp = checkAccess("MODIFICAR_ALUMNO")
    if resp=='true':
        if request.method == 'POST':
            alumno = Estudiante.find_by_id_and_responsable(request.form['idModificar'])
            return redirectUpdateAlumno(None, alumno)
        else:
            return redirect(url_for('listado_alumnos'))
    else:
        return resp

def redirectUpdateAlumno(request = None, alumno = None):
    Barrio.db = get_db()
    Genero.db = get_db()
    Responsable.db = get_db()
    Escuela.db = get_db()
    Nivel.db = get_db()

    barrios = Barrio.all()
    generos = Genero.all()
    responsables = Responsable.all()
    escuelas = Escuela.all()
    niveles = Nivel.all()

    if request:
        return render_template('user/createAlumno.html', barrios = barrios, generos = generos, responsables = responsables, escuelas = escuelas, niveles = niveles, formRequest = request, titulo = "Editar")
    else:
        return render_template('user/createAlumno.html', barrios = barrios, generos = generos, responsables = responsables, escuelas = escuelas, niveles = niveles, alumno = alumno, titulo = "Editar")

def redirectCreateAlumno(request = None):
    Barrio.db = get_db()
    Genero.db = get_db()
    Responsable.db = get_db()
    Escuela.db = get_db()
    Nivel.db = get_db()

    barrios = Barrio.all()
    generos = Genero.all()
    responsables = Responsable.all()
    escuelas = Escuela.all()
    niveles = Nivel.all()

    if request:
        return render_template('user/createAlumno.html', barrios = barrios, generos = generos, responsables = responsables, escuelas = escuelas, niveles = niveles, formRequest = request, titulo = "Registrar")
    else:
        return render_template('user/createAlumno.html', barrios = barrios, generos = generos, responsables = responsables, escuelas = escuelas, niveles = niveles, titulo = "Registrar")

def create():
    if not authenticated(session):
        return render_template('auth/login.html')
    ok=True
    if not pageState():
        ok=False
        for permiso in session['permisos']:
            if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
                ok=True
            #---------------------PERMISOS-----------------------------
    if not ok:
        return render_template('error/mantenimiento.html')
    try:
        if True:
            Estudiante.db = get_db()
            Estudiante.db.autocommit = False
            # apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id
            res = Estudiante.create(  request.form['apellido'],
                                request.form['nombre'],
                                request.form['fecha_nac'],
                                request.form['localidades'],
                                request.form['niveles'],
                                request.form['domicilio'],
                                request.form['generos'],
                                request.form['escuelas'],
                                request.form['tiposDocumento'],
                                request.form['numero'],
                                request.form['tel'],
                                request.form['barrios'] )
            Estudiante.add_responsable(request.form['responsables'], res['idInsertado'])
            Estudiante.db.commit()
            flash("Se creó con éxito", "success")
            return redirect(url_for('listado_alumnos'))
    except Exception as e:
        Estudiante.db.rollback()
        flash(str(e), "danger")
        return redirectCreateAlumno(request.form)

def update():
    if not authenticated(session):
        return render_template('auth/login.html')
    ok=True
    if not pageState():
        ok=False
        for permiso in session['permisos']:
            if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
                ok=True
            #---------------------PERMISOS-----------------------------
    if not ok:
        return render_template('error/mantenimiento.html')

    try:
        if True:

            Estudiante.db = get_db()
            Estudiante.db.autocommit = False
            # apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id
            Estudiante.update(  request.form['apellido'],
                                request.form['nombre'],
                                request.form['fecha_nac'],
                                request.form['localidades'],
                                request.form['niveles'],
                                request.form['domicilio'],
                                request.form['generos'],
                                request.form['escuelas'],
                                request.form['tiposDocumento'],
                                request.form['numero'],
                                request.form['tel'],
                                request.form['barrios'],
                                request.form['id'])

            Estudiante.delete_responsable(request.form['id'])
            Estudiante.add_responsable(request.form['responsables'], request.form['id'])
            flash("Se modificó con éxito", "success")
            return redirect(url_for('listado_alumnos'))
    except Exception as e:
        Estudiante.db.rollback()
        flash(str(e), "danger")
        return redirectUpdateAlumno(request.form)

def alumnoDetalleTemp():
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

    Estudiante.db = get_db()
    estudiante = Estudiante.find_by_id(request.form['user'])
    mapeo=request.form['mapeo']
    tallerId=request.form['tallerId']
    clid=request.form['clid']

    return render_template('user/detalleAlumno.html', user = estudiante, mapeo = mapeo, tallerId=tallerId, clid=clid)

def delete():
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

    try:

        Estudiante.db = get_db()
        
        Estudiante.db.autocommit = False
        # auxEstudiante = Estudiante.find_by_id(request.form['hiddenAluId'])
        # asTaller = Estudiante .asociado_A_Taller(auxEstudiante['id'])
        # if(len(asTaller) == 0):
        Estudiante.delete_responsable_estudiante(request.form['hiddenAluId'])
        Estudiante.remove_estudiante_de_taller(request.form['hiddenAluId'])
        Estudiante.delete(request.form['hiddenAluId'])
        flash("Se eliminó con éxito", "success")
        # else:
        #     flash("El estudiante se encuentra asociado a un taller", "danger")

        Estudiante.db.commit()


        return redirect(url_for('listado_alumnos'))

    except Exception as e:
        flash(str(e), "danger")
        Estudiante.db.rollback()
        return redirect(url_for('listado_alumnos'))
