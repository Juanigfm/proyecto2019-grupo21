from flask import redirect, flash, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers.auth import checkAccess, authenticated
from flaskps.helpers.permissions import usuarioTienePermiso
from flaskps.forms import CreateUserForm
from wtforms import ValidationError
from flaskps.models.roles import Roles
from flaskps.models.estudiantes import Estudiante
from flaskps.models.docentes import Docente
from flaskps.models.taller import Taller
from flaskps.helpers.state import pageState
from flaskps.models.clase import Clase
from flaskps.resources import taller 
import transaction
import re

def deleteClaseDeTaller():
    try:
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
        if not usuarioTienePermiso("ELIMINAR_CLASE"):
            return redirect(url_for('pages_home'))

        Clase.db = get_db()
        Clase.delete(request.form['claseEliminarId'])

        flash("La clase se eliminó con éxito","success")
        return taller.detalle()
    
    except Exception as e:

        msj = str(e)
        # Clase.db.rollback()
        flash(msj, "danger")
        return taller.detalle()

def addClaseATaller():

    try:
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
        if not usuarioTienePermiso("AGREGAR_EDITAR_CLASE"):
            return redirect(url_for('pages_home'))

        Clase.db = get_db()
        Clase.create(request.form['dia'], request.form['inicio'], request.form['fin'], request.form['id'], request.form['docente'])
        # Clase.add_docente_clase(request.form['docente'], res['idInsertado'])
        # Clase.db.commit()

        flash("La clase se agregó con éxito","success")
        return taller.detalle()
    
    except Exception as e:

        msj = str(e)
        # Clase.db.rollback()
        flash(msj, "danger")
        return taller.detalle()


def updateClaseDeTaller():
    try:
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
        if not usuarioTienePermiso("AGREGAR_EDITAR_CLASE"):
            return redirect(url_for('pages_home'))

        Clase.db = get_db()
        Clase.update(request.form['dia'], request.form['inicio'], request.form['fin'], request.form['docente'], request.form['claseEditar'])
        # Clase.add_docente_clase(request.form['docente'], res['idInsertado'])
        # Clase.db.commit()

        flash("La clase se agregó con éxito","success")
        return taller.detalle()
    
    except Exception as e:
        msj = str(e)
        flash(msj, "danger")
        return taller.detalle()

