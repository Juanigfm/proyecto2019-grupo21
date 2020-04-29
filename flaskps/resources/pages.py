from flask import redirect, render_template, request, url_for, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.helpers.auth import authenticated, checkAccess
from flaskps.helpers.state import pageState
from flaskps.helpers.permissions import usuarioTienePermiso
# from flaskps.models.issue import Issue

def index():
    if pageState():
        datos = getByVista('index') #LLAMA A FUNCION DEL CONTROLADOR QUE CONSULTA POR LOS DATOS DEL INDEX
        return render_template('pages/index.html', datos=datos)
    else:
        resp = checkAccess("")
        if resp=='true':
            datos = getByVista('index')
            return render_template('pages/index.html', datos=datos)
        else:
            return resp

def home():
    resp = checkAccess("")
    if resp=='true':
        datos = getByVista('home')
        return render_template('pages/home.html', datos=datos)
    else:
        return resp

def novedades():
    return render_template('pages/novedades.html')

def programacion():
    return render_template('pages/programacion.html')

def nuestras_orquestas():
    return render_template('pages/nuestrasOrquestas.html')

def elegi_tu_instrumento():
    return render_template('pages/eligeTuInstrumento.html')

def biblioteca():
    return render_template('pages/biblioteca.html')

# def talleres():
#     resp = checkAccess("")
#     if resp=='true':
#         return render_template('pages/talleres.html')
#     else:
#         return resp
#
# def cicloLectivo():
#     resp = checkAccess("")
#     if resp=='true':
#         return render_template('pages/cicloLectivo.html')
#     else:
#         return resp

def configuracionSistema():
    resp = checkAccess("CONFIGURACION")
    if not resp=='true':
        return resp

    User.db = get_db()
    Roles.db = get_db()
    # user = User.get_user_by_email(session['email'])
    # roles = Roles.get_roles(user['id'])
    # for p in session['permisos']:
    #     if "CONFIGURACION" in p['nombre']:
    Pages.db = get_db()
    configElems = Pages.all()
    return render_template('pages/configuracionSistema.html', configElems=configElems)
    # else:
    #     #Agregar mensaje de error redirigiendo al login     GONZALO!!!!! GOOOOOOOOOOOOOOOOOOOOOLNZALO!!!!
    #     return redirect(url_for('pages_home'))

def updateConfiguracionSistema():
    resp = checkAccess("")
    if resp=='true':
        ok=True # relleno
    else:
        return resp

    # Obtengo la db ->
    Pages.db = get_db()
    # Actualizo los datos en la db ->
    Pages.updateIndex(request.form['vista'], request.form['titulo'], request.form['cuerpo'], request.form['id'])

    if True:
        flash("La configuración se modificó correctamente.", "success")
        session['feedbackText'] = ""
    else:
        flash("Hubo un error al modificar la configuración.", "danger")

    # Invoco a la funcion para que cargue la página ->
    return redirect(url_for('pages_configuracionSistema'))

def getByVista(nombreVista):
    Pages.db = get_db()
    vistas = Pages.getByVista(nombreVista)

    return vistas

def nucleos():
    resp = checkAccess("")
    if not resp=='true':
        return resp

    Pages.db = get_db()
    nucleos = Pages.getNucleos()
    return render_template('pages/maps.html', nucleos= nucleos)

# def updateEstado(valor):
#     if not authenticated(session):
#         return render_template('auth/login.html')
#     if not pageState():
#         return render_template('error/mantenimiento.html')

#     Pages.db = get_db()
#     Pages.updateEstado(valor)

#     return redirect(url_for('pages_configuracionSistema'))
