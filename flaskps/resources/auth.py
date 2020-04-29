from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.models.permission import Permission
from flaskps import forms
from flaskps.helpers.auth import authenticated
from flaskps.helpers.permissions import usuarioTienePermiso
from flaskps.helpers.state import pageState

def login():
    if not pageState():
        session['mantenimiento'] = "true"
    if not authenticated(session):
        return render_template('auth/login.html')
    return redirect(url_for('pages_home'))

def authenticate():
    params = request.form

    User.db = get_db()
    user = User.find_by_username_or_email_and_pass(params['email'] ,params['email'], params['password'])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for('auth_login'))
    if user['activo'] == 0:
        flash("Cuenta deshabilitada.")
        return redirect(url_for('auth_login'))

    # obtengo los roles del usuario
    Roles.db = get_db()
    roles =  Roles.get_roles(user['id'])
    # obtengo los permisos del usuario (permisos de cada rol)
    Permission.db = get_db()
    permisos = []
    for rol in roles:
        permisos.extend(Permission.all_by_rol(rol['id']))

    # valido si el sitio se encuentra deshabilitado
    Pages.db = get_db()
    estado = Pages.getEstado()
    if int(estado['cuerpo']) == 0:
        ok=False
        for permiso in permisos:
            if not 'VER_EN_MANTENIMIENTO' in permiso:
                ok=True
        if not ok:
            return render_template('error/mantenimiento.html')



    # guardo en la sesión el email, nombre de usuario y todos los permisos
    session['email'] = user['email']
    session['username'] = user['username']
    session['id'] = user['id']
    session['permisos'] = permisos

    session.permanent = True

    # flash("La sesión se inició correctamente.")

    return redirect(url_for('pages_home'))

def logout():
    session.clear()
    return redirect(url_for('auth_login'))

def register():
    return render_template('auth/register.html')

def forgot_pass():
    return render_template('auth/forgot-password.html')
