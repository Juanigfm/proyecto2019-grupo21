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
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
import transaction
import re


def perfil():
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

    User.db = get_db()
    user= User.find_by_id(session['id'])
    return render_template('user/perfil.html', user=user )

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

    msj = "" 
    try:
        formCU = CreateUserForm(request.form) 
        User.db = get_db()
        User.db.autocommit = False
        
        if createIsValid(formCU):
            
            res = User.create(request.form['email'], request.form['usuario'], request.form['password'], request.form['firstName'], request.form['lastName'])
            for rolSelected in request.form.getlist("roles"):
                idRol = int(rolSelected)
                User.add_role(res['idInsertado'], idRol)
            
            User.db.commit()    

            flash("Se creó con éxito", "success")
            return redirect(url_for('listado_usuarios'))


    except Exception as e:
        msj = str(e)
        User.db.rollback()
        rolesUsuario = request.form.getlist("roles")
        roles = Roles.all()
        return render_template("user/registrarUsr.html", titulo = msj, form = formCU, roles= roles, rolesUsuario = rolesUsuario, formRequest= request.form)

def createIsValid(formCU, oldEmail = None, oldUsuario = None, usuarioSesion = False):
    ok = True
    msj=""
    if not formCU.validate():
        ok = False
    if(not re.match(r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$", request.form['email'])):
        ok = False
        formCU.email.errors.append("Ingrese un email válido")
    else:
        #valido si existe el email
        if oldEmail == None or oldEmail != request.form['email']:
            if User.find_by_email(request.form['email']):
                ok = False
                formCU.email.errors.append("El email ya existe")
    if(not re.match(r"^[a-zA-Z0-9]*$", request.form['usuario'])):
        ok = False
        formCU.usuario.errors.append("Solo puede contener caracteres alfanuméricos")
    else:
        #valido si existe el nombre de usuario
        if oldUsuario == None or oldUsuario != request.form['usuario']:
            if User.find_by_username(request.form['usuario']):
                ok = False
                formCU.usuario.errors.append("El usuario ya existe")
    if not usuarioSesion and not request.form.getlist("roles"):
        ok = False
        msj = "Seleccione al menos un rol"
    if not ok:
        raise Exception(msj)
    return ok

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

        User.db = get_db()
        User.db.autocommit = False
        auxUser = User.get_user_by_email(request.form['hiddenEmailD'])
        User.delete(auxUser['id'])
        User.remove_roles_de_usuario(auxUser['id'])

        User.db.commit()

        flash("Se eliminó con éxito", "success")
        return redirect(url_for('listado_usuarios'))

    except Exception as e:
        flash(str(e), "danger")
        User.db.rollback()
        return redirect(url_for('listado_usuarios'))
    
def update():
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
    msj = "" 
    try:
        formCU = CreateUserForm(request.form) 
        User.db = get_db()
        User.db.autocommit = False
        usuarioSesion = int(request.form['id']) == int(session['id'])
        if createIsValid(formCU, request.form['oldEmail'], request.form['oldUsuario'], usuarioSesion):
            # actualizo los datos del usuario
            User.update(request.form['email'], request.form['usuario'], request.form['password'], request.form['firstName'], request.form['lastName'], int(request.form['id']))
            
            if (not usuarioSesion):
                # elimino los roles asociados anteriores
                User.remove_roles_de_usuario(int(request.form['id']))
                # obtengo los roles seleccionados y los agrego
                for rolSelected in request.form.getlist("roles"):
                    idRol = int(rolSelected)
                    User.add_role(int(request.form['id']), idRol)

            msj = "Se modificó con éxito"
            User.db.commit() 
            #si el usuario modifica su propia información de usuario => actualizo los datos de la sesión
            if usuarioSesion:          
                actualizarSession()

            flash("Se modificó con éxito", "success")
            if usuarioSesion:
                return redirect(url_for('user_perfil'))
            else:
                return redirect(url_for('listado_usuarios'))

    except Exception as e:
        msj = str(e)
        User.db.rollback()
        rolesUsuario = request.form.getlist("roles")
        roles = Roles.all()
        user = User.find_by_id(request.form['id'])
        return render_template("user/modificarUsr.html", titulo = msj, user = user ,form = formCU, roles= roles, rolesUsuario = rolesUsuario, usuarioSesion = usuarioSesion, formRequest= request.form)

def actualizarSession():
    session['email'] = request.form['email']
    session['username'] = request.form['usuario']
   
def changeUserState():
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
    if not usuarioTienePermiso("ACTIVAR_USUARIO"):
        return redirect(url_for('pages_home'))

    User.db = get_db()
    auxUser = User.get_user_by_email(request.form['hiddenEmailS'])
    if auxUser['activo'] == 1:
        state = 0
    else:
        state = 1
    User.updateState(state, auxUser['id'])
    
    return redirect(url_for('listado_usuarios'))

def userCreatetTemp():
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
    if not usuarioTienePermiso("CREAR_USUARIO"):
        return redirect(url_for('pages_home'))

    Roles.db = get_db()
    roles = Roles.all()

    return render_template('user/registrarUsr.html', roles = roles)

def userUpdateTemp():
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
    if not usuarioTienePermiso("MODIFICAR_USUARIO"):
        return redirect(url_for('pages_home'))

    User.db = get_db()
    user = User.get_user_by_email(request.form['email'])
    Roles.db = get_db()
    roles = Roles.all()
    usuarioSesion = user['id'] == session['id']
    rolesUsuario = Roles.get_roles(user['id'])

    return render_template('user/modificarUsr.html', user = user, roles = roles, usuarioSesion= usuarioSesion, rolesUsuario = rolesUsuario)

def listadoUsuarios(params = { "init" : 0 }, function=1, activo = None, nombre = ''):
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
    if not usuarioTienePermiso("LISTADO_USUARIOS"):
        return redirect(url_for('pages_home'))

    
    Pages.db = get_db()
    paginado = Pages.get_paginado()
    params['pag'] = int(paginado['cuerpo'])

    if request.method == 'POST' and 'init' in request.form.keys() and int(request.form['init'])>=0:
        params ['init'] = int(request.form['init'])

    filtro=''

    if ('estadoFiltro' in request.form.keys()):
        if (request.form['estadoFiltro'] == '1' or request.form['estadoFiltro'] == '0'):
            activo = request.form['estadoFiltro']
            function=0
            filtro=request.form['estadoFiltro']
    if ('nombreFiltro' in request.form.keys()):
        if (request.form['nombreFiltro'] and request.form['nombreFiltro'].strip()):
            nombre = request.form['nombreFiltro']
            function=0
            filtro=request.form['nombreFiltro']

    User.db = get_db()
    user = User.get_user_by_email(session['email'])
    users = User.get_listado(user['id'], activo, nombre)

    return render_template('user/listado.html', users=users, params=params, nombreFiltro=nombre, activoFiltro=activo, function=function, filtro=filtro)

def update_profile():
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
          
    # actualizo los datos del usuario
    User.db = get_db()
    User.update_profile(request.form['email'], request.form['usuario'], request.form['firstName'], request.form['lastName'], int(request.form['id']))
    session['email'] = str(request.form['email'])
    session['username'] = str(request.form['usuario'])
    return redirect(url_for('user_perfil'))

def update_password():
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


# def update_profile():
#     if not authenticated(session):
#         return render_template('auth/login.html')
#     if not pageState():
#         return render_template('error/mantenimiento.html')
          
#     # actualizo los datos del usuario
#     User.db = get_db()
#     User.update_profile(request.form['email'], request.form['usuario'], request.form['firstName'], request.form['lastName'], int(request.form['id']))
#     session['email'] = str(request.form['email'])
#     session['username'] = str(request.form['usuario'])
#     return redirect(url_for('user_perfil'))

# def update_password():
#     if not authenticated(session):
#         return render_template('auth/login.html')
#     if not pageState():
#         return render_template('error/mantenimiento.html')
          
#     # actualizo los datos del usuario
#     User.db = get_db()
#     User.update_password(request.form['newpassword'], int(request.form['id']))
#     return redirect(url_for('user_perfil'))
    
# # def deactivate():
# #     if not authenticated(session):
# #         abort(401)

# #     User.db =get_db()
# #     User.deactivate(request.form['id'])

# def buscar():
    # User.db = get_db()
    # if request.content_length==5:
        # busqueda = User.buscar(str(1), str(request.form['usuario']), str(request.form['email']), str(request.form['nombre']), str(request.form['apellido']))
    # else:
        #  busqueda = User.buscar(str(0), request.form['usuario'], request.form['email'], request.form['nombre'], request.form['apellido'])
    
    