function validarCrearTaller(){
    
    var ok = true;
    //-------------------------------VALIDO NOMBRE------------------------------------
    nombre = document.getElementById('nombre').value;
    spanNombre = document.getElementById('spanNombre');
    if (nombre == ''){
         ok = false;
         spanNombre.innerHTML = 'Ingrese un nombre';
    }else{
        spanNombre.innerHTML = '';
    }

    //-------------------------------VALIDO NOMBRE CORTO------------------------------------
    nombre = document.getElementById('nombrecorto').value;
    spanNombre = document.getElementById('spanNombreCorto');
    if (nombre == ''){
         ok = false;
         spanNombre.innerHTML = 'Ingrese un nombre corto';
    }else{
        spanNombre.innerHTML = '';
    }

    //------------------------------VALIDO NUCLEO------------------------
    if(document.getElementById('nucleo') != null){
        nucleo = document.getElementById('nucleo').value;
        spanNucleo = document.getElementById('spanNucleo');
        if (nucleo == "0"){
            ok = false;
            spanNucleo.innerHTML = 'Seleccione un nucleo';
        }else{
            spanNucleo.innerHTML = '';
        }
    }

    //------------------------------VALIDO CICLO------------------------
    if(document.getElementById('ciclo') != null){
        ciclo = document.getElementById('ciclo').value;
        spanCiclo = document.getElementById('spanCiclo');
        if (ciclo == "0"){
             ok = false;
             spanCiclo.innerHTML = 'Seleccione un ciclo lectivo';
        }else{
            spanCiclo.innerHTML = '';
        }
    }

    if (ok){
        var formAgregar = document.forms['formAgregar'];
        formAgregar.submit();
    }
}

function validarAddTallerACiclo(){
    
    var ok = true;

    //------------------------------VALIDO TALLER------------------------
    taller = document.getElementById('idTaller').value;
    spanTaller = document.getElementById('spanTaller');
    if (taller == "0"){
         ok = false;
         spanTaller.innerHTML = 'Seleccione un taller';
    }else{
        spanTaller.innerHTML = '';
    }
    if (ok){
        var form = document.forms['formAddTallerACiclo'];
        form.submit();
    }
}

function validarAddAlumnoATaller(){
    
    var ok = true;

    //------------------------------VALIDO TALLER------------------------
    alumno = document.getElementById('alumno').value;
    spanAlumno = document.getElementById('spanAlumno');
    if (alumno == "0"){
         ok = false;
         spanAlumno.innerHTML = 'Seleccione un alumno';
    }else{
        spanAlumno.innerHTML = '';
    }
    if (ok){
        var form = document.forms['formAddAlumnoATaller'];
        form.submit();
    }
}

function validarAddDocenteATaller(){
    
    var ok = true;

    //------------------------------VALIDO Docente------------------------
    docente = document.getElementById('docenteAdd').value;
    spanDocente = document.getElementById('spanDocente');
    if (docente == "0"){
         ok = false;
         spanDocente.innerHTML = 'Seleccione un docente';
    }else{
        spanDocente.innerHTML = '';
    }
    if (ok){
        var form = document.forms['formAddDocenteATaller'];
        form.submit();
    }
}

function validarVerAistencia(){
    
    var ok = true;

    //------------------------------VALIDO VER ASISTENCIA------------------------
    taller = document.getElementById('idlog').value;
    spanClase = document.getElementById('spanClase');
    if (taller == "0"){
         ok = false;
         spanClase.innerHTML = 'Seleccione una clase';
    }else{
        spanClase.innerHTML = '';
    }
    if (ok){
        var form = document.forms['formVerAsistencia'];
        form.submit();
    }
}


function validarTomarAsistencia(){
    
    var ok = true;

    //------------------------------VALIDO TOMAR ASISTENCIA------------------------
    clase = document.getElementById('clase').value;
    span = document.getElementById('span');
    fecha = document.getElementById('fecha').value;
    var today = new Date();
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    if(clase == "0" & fecha == "" ){
        ok = false;
        span.innerHTML = 'Seleccione una clase y una fecha';
    }else{
        if (clase == "0"){
            ok = false;
            span.innerHTML = 'Seleccione una clase';
       }else{
            if (fecha == ""){
                ok = false;
                span.innerHTML = 'Seleccione una fecha';
            }else{
                if (fecha > date){
                    ok = false;
                    span.innerHTML = 'Seleccione una fecha menor o igual a la actual'
                }
                else{
                    span.innerHTML = '';
                }
            }
        }
    }    
    if (ok){
        var lista = $("input:checkbox");
        var presentes = 0;
        for (var i = 0; i < lista.length; i++) {
            if(lista[i].checked){
                presentes++;
                break;
            }
        }
        $("#deleteEmployeeModal").modal();
        if(presentes==0){
            document.getElementById("smallTexto").innerHTML = "Todos las alumnos se registraran como AUSENTE";
        }else{
            document.getElementById("smallTexto").innerHTML = "Todos los alumnos no marcados se registraran como AUSENTE";
        }
    }
}

function submitTomarAsistencia(){
    var form = document.forms['formTomarAsistencia'];
    form.submit();
}
