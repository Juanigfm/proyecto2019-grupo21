from os import path
from flask import Flask, render_template, g
from flaskps.resources import pages
from flaskps.resources import user
from flaskps.resources import auth
from flaskps.resources import error
from flaskps.resources import alumno
from flaskps.resources import docente
from flaskps.resources import taller
from flaskps.resources import ciclos
from flaskps.resources import instrumentos
from flaskps.resources import clase
from flaskps.resources import asistencia
from flaskps.config import Config

# Configuración inicial de la app
app = Flask(__name__)
app.config.from_object(Config)

# Autenticación
app.add_url_rule("/forgot-password", 'auth_forgot_pass', auth.forgot_pass)
app.add_url_rule("/register", 'auth_register', auth.register)
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule("/auth", 'auth_authenticate', auth.authenticate, methods=['POST'])

# Consultas/Pages
app.add_url_rule("/", 'pages_index', pages.index)
app.add_url_rule("/pages/home", 'pages_home', pages.home)
app.add_url_rule("/pages/novedades", 'pages_novedades', pages.novedades)
app.add_url_rule("/pages/programacion", 'pages_programacion', pages.programacion)
app.add_url_rule("/pages/nuestrasorquestas", 'pages_nuestras_orquestas', pages.nuestras_orquestas)
app.add_url_rule("/pages/elegituinstrumento", 'pages_elegi_tu_instrumento', pages.elegi_tu_instrumento)
app.add_url_rule("/pages/biblioteca", 'pages_biblioteca', pages.biblioteca)
app.add_url_rule("/pages/configuracionSistema", 'pages_configuracionSistema', pages.configuracionSistema)
app.add_url_rule("/pages/updateConfig", 'pages_configUpdate', pages.updateConfiguracionSistema, methods=['POST'])
app.add_url_rule("/pages/nucleos", 'pages_maps', pages.nucleos, methods=['GET', 'POST'])
# app.add_url_rule("/pages/talleres", 'pages_talleres', pages.talleres)
# app.add_url_rule("/pages/cicloLectivo", 'pages_cicloLectivo', pages.cicloLectivo)

# Usuarios
app.add_url_rule("/usuarios/perfil", 'user_perfil', user.perfil)
app.add_url_rule("/usuarios/delete", 'user_delete', user.delete, methods=['POST'])
app.add_url_rule("/usuarios/listadoUsuarios", 'listado_usuarios', user.listadoUsuarios, methods=['GET','POST'])
app.add_url_rule("/usuarios/create", 'user_create', user.create, methods=['POST'])
app.add_url_rule("/usuarios/update", 'user_update', user.update, methods=['POST'])
app.add_url_rule("/usuarios/changeUserState", 'user_changeUserState', user.changeUserState, methods=['POST'])
app.add_url_rule("/usuarios/createTemp", 'user_create_temp', user.userCreatetTemp)
app.add_url_rule("/usuarios/updateTemp", 'user_update_temp', user.userUpdateTemp, methods=['POST'])
# app.add_url_rule("/usuarios/busqueda", 'user_buscar', user.buscar, methods=['POST'])
# app.add_url_rule("/usuarios/updateprofile", 'user_updateprofile', user.update_profile, methods=['POST'])
# app.add_url_rule("/usuarios/updatepassword", 'user_updatepassword', user.update_password, methods=['POST'])

# Alumnos
app.add_url_rule("/usuarios/listadoAlumnos", 'listado_alumnos', alumno.listadoAlumnos, methods=['GET','POST'])
# app.add_url_rule("/usuarios/createAlumnoTemp", 'alumno_create_temp', alumno.alumnoCreateTemp)
# app.add_url_rule("/usuarios/createAlumno", 'alumno_create', alumno.create)
app.add_url_rule("/usuarios/detalleAlumno", 'alumno_detalle_temp', alumno.alumnoDetalleTemp, methods=['POST'])
app.add_url_rule("/usuarios/createAlumnoTemp", 'alumno_create_temp', alumno.alumnoCreateTemp, methods=['GET','POST'])
app.add_url_rule("/usuarios/updateAlumnoTemp", 'alumno_update_temp', alumno.alumnoUpdateTemp, methods=['GET','POST'])
app.add_url_rule("/usuarios/createAlumno", 'alumno_create', alumno.create, methods=['POST'])
app.add_url_rule("/usuarios/updateAlumno", 'alumno_update', alumno.update, methods=['POST'])
app.add_url_rule("/usuarios/deleteAlumno", 'alumno_delete', alumno.delete, methods=['POST'])

# Docentes
app.add_url_rule("/usuarios/listadoDocentes", 'listado_docentes', docente.listadoDocentes, methods=['GET','POST'])
# app.add_url_rule("/usuarios/agregarDocentes", 'docente_add', docente.docente_add, methods=['GET','POST'])
# app.add_url_rule("/usuarios/createDocente", 'docente_create', docente.create)
# app.add_url_rule("/usuarios/createDocenteTemp", 'docente_create_temp', docente.docenteCreateTemp)
# app.add_url_rule("/usuarios/detalleDocenteTemp", 'docente_detalle_temp', docente.docenteDetalleTemp, methods=['POST'])
# app.add_url_rule("/usuarios/deleteDocente", 'docente_delete', docente.delete, methods=['POST'])
app.add_url_rule("/usuarios/detalleDocente", 'docente_detalle_temp', docente.docenteDetalleTemp, methods=['POST'])
app.add_url_rule("/usuarios/createDocenteTemp", 'docente_create_temp', docente.docenteCreateTemp, methods=['GET','POST'])
app.add_url_rule("/usuarios/updateDocenteTemp", 'docente_update_temp', docente.docenteUpdateTemp, methods=['GET','POST'])
app.add_url_rule("/usuarios/createDocente", 'docente_create', docente.create, methods=['POST'])
app.add_url_rule("/usuarios/updateDocente", 'docente_update', docente.update, methods=['POST'])
app.add_url_rule("/usuarios/deleteDocente", 'docente_delete', docente.delete, methods=['POST'])

# Instrumentos
app.add_url_rule("/pages/instrumentos_lista", 'instrumentos_lista', instrumentos.instrumentos_lista, methods=['GET','POST'])
app.add_url_rule("/pages/instrumentos_detalle", 'instrumentos_detalle', instrumentos.instrumentos_detalle, methods=['POST'])
app.add_url_rule("/pages/instrumentos_nuevo", 'instrumentos_nuevo', instrumentos.instrumentos_nuevo, methods=['GET','POST'])
app.add_url_rule("/pages/instrumentos_modificar", 'instrumentos_modificar', instrumentos.instrumentos_modificar, methods=['POST'])
app.add_url_rule("/pages/instrumentos_borrar", 'instrumentos_borrar', instrumentos.instrumentos_borrar, methods=['POST'])
app.add_url_rule("/pages/instrumentos_create", 'instrumentos_create', instrumentos.instrumentos_create, methods=['POST'])
app.add_url_rule("/pages/instrumentos_update", 'instrumentos_update', instrumentos.instrumentos_update, methods=['POST'])

# Talleres
app.add_url_rule("/talleres/listadoTalleres", 'listado_talleres', taller.listado_talleres, methods=['GET','POST'])
app.add_url_rule("/talleres/tallerAlumnoTemp", 'taller_create_temp', taller.tallerCreatetTemp, methods=['GET','POST'])
app.add_url_rule("/talleres/createTaller", 'taller_create', taller.create, methods=['POST'])
app.add_url_rule("/talleres/detalleTaller", 'taller_detalle', taller.detalle, methods=['POST'])
app.add_url_rule("/talleres/agregarDocente", 'taller_agregar_docente', taller.agregar_docente, methods=['POST'])
app.add_url_rule("/talleres/agregarAlumno", 'taller_agregar_alumno', taller.agregar_alumno, methods=['POST'])
app.add_url_rule("/talleres/bajaDocente", 'taller_baja_docente', taller.baja_docente, methods=['POST'])
app.add_url_rule("/talleres/bajaAlumno", 'taller_baja_alumno', taller.baja_alumno, methods=['POST'])

# Ciclos
app.add_url_rule("/ciclos/listadoCiclos", 'listado_ciclos', ciclos.listado_ciclos, methods=['POST','GET'])
app.add_url_rule("/talleres/createCicloTemp", 'ciclo_create_temp', ciclos.cicloCreatetTemp)
app.add_url_rule("/ciclos/createCiclo", 'ciclo_create', ciclos.create, methods=['POST','GET'])
app.add_url_rule("/ciclos/detalleCiclo", 'ciclo_detalle', ciclos.detalle, methods=['POST','GET'])
# app.add_url_rule("/ciclos/addTaller", 'ciclo_add_taller_temp', ciclos.addTaller, methods=['POST'])
app.add_url_rule("/ciclos/ciclosEliminar", 'ciclo_delete', ciclos.delete, methods=['POST'])
app.add_url_rule("/ciclos/ciclosModificar", 'ciclo_update', ciclos.update, methods=['POST'])
app.add_url_rule("/ciclos/ciclosModificarTemp", 'ciclo_update_temp', ciclos.updateTemp, methods=['POST'])
app.add_url_rule("/ciclos/createTaller", 'ciclo_create_taller_temp', ciclos.createTaller, methods=['POST'])

# Clase
app.add_url_rule("/clase/addClase", 'add_clase', clase.addClaseATaller, methods=['POST'])
app.add_url_rule("/clase/deleteClase", 'delete_clase', clase.deleteClaseDeTaller, methods=['POST'])
app.add_url_rule("/clase/updateClase", 'update_clase', clase.updateClaseDeTaller, methods=['POST'])

# Asistencia

app.add_url_rule("/asistencia/tomarAsistencia", 'tomar_asistencia_temp', asistencia.tomarAsistenciaTemp, methods=['POST'])
app.add_url_rule("/asistencia/registrarAsistencias", 'registrar_asistencias', asistencia.registrarAsistencias, methods=['POST'])
app.add_url_rule("/asistencia/verAsistencias",'ver_asistencias',asistencia.verAsistencias, methods=['POST'])

# API-rest
# app.add_url_rule("/api/consultas", 'api_issue_index', api_issue.index)

# Error
app.add_url_rule("/404-notfound", '404-notfound', error.notfound)
app.add_url_rule("/mantenimiento", 'mantenimiento', error.mantenimiento)

# Error genérico
app.register_error_handler(405, error.handle_bad_request)

#@app.route("/")
# def hello():
#     return render_template('pages/index.html')
