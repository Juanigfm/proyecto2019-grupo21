from flask import redirect, render_template, request, url_for, session, flash
from os import path, remove, rename
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.roles import Roles
from flaskps.models.pages import Pages
from flaskps.models.tipo_instrumento import TipoInstrumento
from flaskps.models.instrumentos import Instrumento
from flaskps.helpers.auth import checkAccess
from flaskps.helpers.permissions import usuarioTienePermiso

pathUrl='grupo21/flaskps/static/uploads'
# pathUrl='flaskps/static/uploads'

# Al template
def instrumentos_lista(params = { "init" : 0 }, function=1, activo = None, nombre = ''):
    resp = checkAccess("LISTADO_INSTRUMENTOS")
    if not resp=='true':
        return resp

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

    Instrumento.db = get_db()
    users = Instrumento.get_listado(nombre)

    return render_template('pages/instrumentos_lista.html', users=users, params=params, nombreFiltro=nombre, function=function, filtro=filtro)

# Al template
def instrumentos_detalle():
    resp = checkAccess("DETALLE_INSTRUMENTO")
    if not resp=='true':
        return resp

    #Carga los datos de la BD
    Instrumento.db = get_db()
    instrumento = Instrumento.find_by_id(request.form['hiddenid'])

    # Checkear existencia de img
    # pathUrl="flaskps"+url_for('static', filename='uploads/')
    if path.isfile(path.join(pathUrl, instrumento['imagen'])):
        imagen=url_for('static', filename='uploads/'+instrumento['imagen'])
    else:
        imagen=url_for('static', filename='uploads/not_found.jpg')

    #Ver de ruta
    import os
    test=os.getcwd()

    return render_template('pages/instrumentos_detalle.html', titulo = "Detalle", instrumento=instrumento, imagen=imagen, test=test)

# Formulario
class FormInstrumento(Form):
    Nombre = TextField('Nombre',
        validators=[validators.required(message='Requerido '),
                    validators.length(min=3, max=15, message='De 3 a 15 caracteres. '),
                    validators.Regexp('^[a-zA-Z]\w+$', message='Solo letras, numeros o "_". Debe comenzar con una letra. ')])
    Tipo = SelectField('Tipo',
        coerce=int,
        choices=[(1, ""), (2, ""), (3, "")],
        validators=[validators.required(message='Seleccione una opcion. ')])
    Identificador = TextField('Identificador',
        validators=[validators.required(message='Requerido'),
                    validators.length(min=3, max=15, message='De 3 a 15 caracteres. '),
                    validators.Regexp('^[a-zA-Z]\w+$', message='Solo letras, numeros o "_". Debe comenzar con una letra. ')])

def check_img(f_extension):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    if f_extension.lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        flash("Error, solo se permiten imagenes (png, jpg, jpeg)", "danger")
        return False

# Al template
def instrumentos_nuevo(form = None):
    resp = checkAccess("CREAR_INSTRUMENTO")
    if not resp=='true':
        return resp

    if form is None: #Formulario en blanco
        form=FormInstrumento()
        instrumento=None
    else: #Carga los datos del formulario enviado
        instrumento= {
            'nombre':request.form['Nombre'],
            'tipo_id':int(request.form['Tipo']),
            'codigo':request.form['Identificador']
        }

    imagenActual=url_for('static', filename='uploads/no_image.jpeg')

    TipoInstrumento.db = get_db()
    tipos = TipoInstrumento.all()

    return render_template('pages/instrumentos_nuevo.html', titulo = "Nuevo", tipos=tipos, form = form, instrumento=instrumento, imagenActual=imagenActual)

# Al template
def instrumentos_modificar(form = None):
    resp = checkAccess("MODIFICAR_INSTRUMENTO")
    if not resp=='true':
        return resp

    Instrumento.db = get_db()
    eliminarImg={'estado':"",'valor':""}
    if form is None: #Carga los datos de la BD
        instrumento = Instrumento.find_by_id(request.form['idModificar'])
        img= instrumento['imagen']
    else: #Carga los datos del formulario enviado
        instrumento= {
            'nombre':request.form['Nombre'],
            'tipo_id':int(request.form['Tipo']),
            'codigo':request.form['Identificador'],
            'id':request.form['id']
        }
        instrumentoBD = Instrumento.find_by_id(instrumento['id'])
        img= instrumentoBD['imagen']
        if 'EliminarImg' in request.form:
            eliminarImg['valor']="checked"

    # Checkear existencia de img
    # pathUrl="flaskps"+url_for('static', filename='uploads/')
    if path.isfile(path.join(pathUrl, img)):
        imagenActual=url_for('static', filename='uploads/'+img)
    else:
        imagenActual=url_for('static', filename='uploads/not_found.jpg')

    # Eliminar img checkbox
    if img=="no_image.jpeg":
        eliminarImg['estado']="disabled"

    TipoInstrumento.db = get_db()
    tipos = TipoInstrumento.all()

    return render_template('pages/instrumentos_nuevo.html', titulo = "Modificar", tipos=tipos, form = form, instrumento=instrumento, imagenActual=imagenActual, eliminarImg=eliminarImg)

# Base de datos
def instrumentos_create():
    resp = checkAccess("CREAR_INSTRUMENTO")
    if not resp=='true':
        return resp

    form=FormInstrumento(request.form)

    Nombre=request.form['Nombre']
    Tipo=request.form['Tipo']
    Identificador=request.form['Identificador']

    if not form.validate():
        flash("Error", "danger")
        return instrumentos_nuevo(form)

    # Checkear codigo existente
    Instrumento.db = get_db()
    instrumento = Instrumento.buscar_codigo(Identificador)
    if instrumento!=None:
        flash("Error, el IDENTIFICADOR ya existe", "danger")
        return instrumentos_nuevo(form)

    # Guardar imagen
    f = request.files['Imagen']
    if f.filename!="":
        f_extension = f.filename.split('.')[1]
        if not check_img(f_extension):
            return instrumentos_nuevo(form)
        Imagen="imgID"+request.form['Identificador']+"."+f_extension
        # pathUrl="flaskps"+url_for('static', filename='uploads/')
        f.save(path.join(pathUrl, Imagen))
    else:
        Imagen="no_image.jpeg"

    try:
        # Instrumento.db = get_db()
        Instrumento.db.autocommit = False
        Instrumento.create(
            request.form['Nombre'],
            request.form['Tipo'],
            request.form['Identificador'],
            Imagen
        )
        Instrumento.db.commit()

        flash("Se creó con éxito", "success")
        return redirect(url_for('instrumentos_lista'))

    except Exception as e:
        flash(str(e), "danger")
        Instrumento.db.rollback()
        # return instrumentos_nuevo(request.form)
        return instrumentos_nuevo(form)

# Base de datos
def instrumentos_update():
    resp = checkAccess("MODIFICAR_INSTRUMENTO")
    if not resp=='true':
        return resp

    form=FormInstrumento(request.form)

    Nombre=request.form['Nombre']
    Tipo=request.form['Tipo']
    Identificador=request.form['Identificador']

    if not form.validate():
        flash("Error", "danger")
        return instrumentos_modificar(form)

    # Checkear codigo existente
    Instrumento.db = get_db()
    instrumento = Instrumento.buscar_codigo(Identificador)
    if instrumento!=None:
        cambioDeCodigo=False
        if instrumento['id']!=int(request.form['id']):
            flash("Error, el IDENTIFICADOR ya existe", "danger")
            return instrumentos_modificar(form)
    else:
        cambioDeCodigo=True

    # Guardar imagen
    instrumento = Instrumento.find_by_id(request.form['id'])
    # pathUrl="flaskps"+url_for('static', filename='uploads/')
    original=path.join(pathUrl, instrumento['imagen'])
    f = request.files['Imagen']
    if f.filename!="":
        f_extension = f.filename.split('.')[1]
        if not check_img(f_extension):
            return instrumentos_modificar(form)
        Imagen="imgID"+request.form['Identificador']+"."+f_extension
        # Borrar img vieja
        if instrumento['imagen']!="no_image.jpeg" and instrumento['imagen']!="" and path.isfile(original):
            remove(original)
        # Guardar nueva
        f.save(path.join(pathUrl, Imagen))
    elif 'EliminarImg' in request.form:
        Imagen="no_image.jpeg"
        # Borrar img
        if instrumento['imagen']!="no_image.jpeg" and instrumento['imagen']!="" and path.isfile(original):
            remove(original)
    else:
        Imagen=""
        if instrumento['imagen']!="no_image.jpeg":
            if cambioDeCodigo:
                # Renombrar imagen
                f_extension = instrumento['imagen'].split('.')[1]
                Imagen="imgID"+request.form['Identificador']+"."+f_extension
                if path.isfile(original):
                    rename(original, path.join(pathUrl, Imagen))
            else:
                if instrumento['imagen']=="":
                    Imagen="no_image.jpeg"

    try:
        # Instrumento.db = get_db()
        Instrumento.db.autocommit = False
        if Imagen=="":
            Instrumento.updateNoImg(
                request.form['Nombre'],
                request.form['Tipo'],
                request.form['Identificador'],
                request.form['id']
            )
        else:
            Instrumento.update(
                request.form['Nombre'],
                request.form['Tipo'],
                request.form['Identificador'],
                Imagen,
                request.form['id']
            )
        Instrumento.db.commit()

        flash("Se modifico con éxito", "success")
        return redirect(url_for('instrumentos_lista'))

    except Exception as e:
        flash(str(e), "danger")
        Instrumento.db.rollback()
        # return instrumentos_modificar(request.form)
        return instrumentos_modificar(form)

# Base de datos
def instrumentos_borrar():
    resp = checkAccess("ELIMINAR_INSTRUMENTO")
    if not resp=='true':
        return resp

    # Borrar img
    Instrumento.db = get_db()
    instrumento = Instrumento.find_by_id(request.form['hiddenAluId'])
    if instrumento['imagen']!="no_image.jpeg" and instrumento['imagen']!="":
        # pathUrl="flaskps"+url_for('static', filename='uploads/')
        urlImg=path.join(pathUrl, instrumento['imagen'])
        if path.isfile(urlImg):
            remove(urlImg)

    try:
        # Instrumento.db = get_db()
        Instrumento.db.autocommit = False
        Instrumento.delete(request.form['hiddenAluId'])
        Instrumento.db.commit()

        flash("Se eliminó con éxito", "success")
        return redirect(url_for('instrumentos_lista'))

    except Exception as e:
        flash(str(e), "danger")
        Instrumento.db.rollback()
        return redirect(url_for('instrumentos_lista'))
