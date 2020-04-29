from flask import redirect, render_template, request, url_for, session
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso

def authenticated(session):
    return session.get('email')

def checkAccess(permiso):
    if not authenticated(session):
        return redirect(url_for('auth_login'))
    ok=True
    if not pageState():
        ok=False
        for permiso in session['permisos']:
            if "VER_EN_MANTENIMIENTO" == permiso['nombre']:
                ok=True
    if not ok:
        return redirect(url_for('mantenimiento'))
    if not permiso == "":
        if not usuarioTienePermiso(permiso):
            return redirect(url_for('pages_home'))
    return "true"
