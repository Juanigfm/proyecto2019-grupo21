from flask import redirect, flash, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.helpers.auth import authenticated, checkAccess
from flaskps.forms import CreateUserForm
from wtforms import ValidationError
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.models.docentes import Docente
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
from flaskps.models.genero import Genero
from flaskps.models.clase import Clase
from flaskps.models.taller import Taller
import transaction
import re

def listadoDocentes(params = { "init" : 0 }, function=1, activo = None, nombre = ''):
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
    if not usuarioTienePermiso("LISTADO_DOCENTES"):
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
    # PARA USUARIO PERO HAYQ UE AGREGAR LOS FILTROS PARA LA BUSQUEDA
    Docente.db = get_db()
    users = Docente.get_listado(nombre)

    return render_template('user/listadoDocentes.html', users=users, params=params, nombreFiltro=nombre, function=function, filtro=filtro)

def docenteCreateTemp():
    resp = checkAccess("CREAR_DOCENTE")
    if resp=='true':
        return redirectCreateDocente()
    else:
        return resp

def docenteUpdateTemp():
    resp = checkAccess("MODIFICAR_DOCENTE")
    if resp=='true':
        if request.method == 'POST':
            docente = Docente.find_by_id(request.form['idModificar'])
            return redirectUpdateDocente(None, docente)
        else:
            return redirect(url_for('listado_docentes'))
    else:
        return resp

def redirectUpdateDocente(request = None, docente = None):
    Genero.db = get_db()
    generos = Genero.all()
    if request:
        return render_template('user/createDocente.html', generos = generos, formRequest = request, titulo = "Editar")
    else:
        return render_template('user/createDocente.html', generos = generos, docente = docente, titulo = "Editar")

def redirectCreateDocente(request = None):
    Genero.db = get_db()
    generos = Genero.all()
    if request:
        return render_template('user/createDocente.html', generos = generos, formRequest = request, titulo = "Registrar")
    else:
        return render_template('user/createDocente.html', generos = generos, titulo = "Registrar")

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
            Docente.db = get_db()
            # Docente.db.autocommit = False
            # apellido, nombre, fecha_nac, localidad_id, domicilio, tipo_doc_id, numero, tel
            Docente.create(  request.form['apellido'],
                                request.form['nombre'],
                                request.form['fecha_nac'],
                                request.form['localidades'],
                                request.form['domicilio'],
                                request.form['generos'],
                                request.form['tiposDocumento'],
                                request.form['numero'],
                                request.form['tel'] )
            # Docente.add_responsable(request.form['responsables'], res['idInsertado'])
            # Docente.db.commit()
            flash("Se creó con éxito", "success")
            return redirect(url_for('listado_docentes'))
    except Exception as e:
        # Docente.db.rollback()
        flash(str(e), "danger")
        return redirectCreateDocente(request.form)

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

            Docente.db = get_db()
            # Docente.db.autocommit = False
            # apellido, nombre, fecha_nac, localidad_id, domicilio, tipo_doc_id, numero, tel
            Docente.update(  request.form['apellido'],
                                request.form['nombre'],
                                request.form['fecha_nac'],
                                request.form['localidades'],
                                request.form['domicilio'],
                                request.form['generos'],
                                request.form['tiposDocumento'],
                                request.form['numero'],
                                request.form['tel'],
                                request.form['id'])

            # Docente.delete_responsable(request.form['id'])
            # Docente.add_responsable(request.form['responsables'], request.form['id'])
            flash("Se modificó con éxito", "success")
            return redirect(url_for('listado_docentes'))
    except Exception as e:
        # Docente.db.rollback()
        flash(str(e), "danger")
        return redirectUpdateDocente(request.form)


def docenteDetalleTemp():
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
    # if not usuarioTienePermiso("MODIFICAR_USUARIO"):
    #     return redirect(url_for('pages_home'))

    Docente.db = get_db()
    Clase.db = get_db()
    docente = Docente.find_by_id(request.form['user'])
    clases = Clase.get_clases_by_docente(request.form['user'])
    # Roles.db = get_db()
    # roles = Roles.all()
    # usuarioSesion = user['id'] == session['id']
    # rolesUsuario = Roles.get_roles(user['id'])
    mapeo=request.form['mapeo']
    tallerId=request.form['tallerId']
    clid=request.form['clid']

    return render_template('user/detalleDocente.html', user = docente, mapeo = mapeo, tallerId=tallerId, clid=clid, clases=clases)

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
        Taller.db = get_db()
        #valido que el docente no tenga talleres asignados
        talleres = Taller.get_talleres_con_clases_de_docente(request.form['hiddenDocId'])
        msj=""
        if len(talleres) > 0:
            for t in talleres:
                msj = msj + t['nombre'] + ", "
            msj = "El docente actualmente dicta clases en el/los talleres: "+ msj +"para eliminarlo desasignelo"
            flash(msj,"danger")
        else:
            Docente.db = get_db()
            Docente.db.autocommit = False
            # auxDocente = Docente.find_by_id(request.form['hiddenDocId'])
            # asTaller = Docente.asociado_A_Taller(auxDocente['id'])

            # if(len(asTaller) == 0):
            Docente.remove_docente_de_taller(request.form['hiddenDocId'])
            Docente.delete(request.form['hiddenDocId'])
            flash("Se eliminó con éxito", "success")
            # else:
            #     flash("El docente se encuentra asociado a un taller", "danger")

            Docente.db.commit()

        return redirect(url_for('listado_docentes'))

    except Exception as e:
        flash(str(e), "danger")
        Docente.db.rollback()
        return redirect(url_for('listado_docentes'))
