function eliminarTaller(id){
    document.getElementById('claseEliminarId').value = id;
}

function editClase(claseId, dia, horaInicio, horaFin, docenteId){
    document.getElementById('inicio').value = horaInicio;
    document.getElementById('fin').value = horaFin;
    document.getElementById('dia').value = dia;
    document.getElementById('claseEditar').value = claseId;
    document.getElementById('docente').value = docenteId;

    document.getElementById('nombre').innerHTML = 'Editar clase';
    document.getElementById('inputAgregar').style.display = 'none';
    document.getElementById('inputEditar').style.display = '';
    document.getElementById('inputCancelar').style.display = '';
    document.getElementById('formAddClaseATaller').action="/clase/updateClase";
}

function validar(){
    var ok = true;
    spanClase = document.getElementById('spanClase');
    spanClase.innerHTML = '';
    
    // ------------------------VALIDO HORARIOS-------------------------------
    inicio = document.getElementById('inicio').value;
    fin = document.getElementById('fin').value;
    if (inicio == '' || fin == ''){
         ok = false;
         spanClase.innerHTML = spanClase.innerHTML + 'Ingrese un horario válido. ';
    }else{
        var t1 = inicio.split(":");
        var horaInicio = t1[0];
        var minInicio = t1[1];
        var t2 = fin.split(":");
        var horaFin = t2[0];
        var minFin = t2[1];

        if(horaInicio > horaFin){
            ok = false;
            spanClase.innerHTML = spanClase.innerHTML + 'La hora de inicio no puede ser mayor a la de fin. ';
        }else{
            if(horaInicio == horaFin && minInicio >= minFin){
                ok = false;
                spanClase.innerHTML = spanClase.innerHTML + 'La hora de inicio no puede ser mayor o igual a la de fin. ';
            }
        }
    }

    //-------------------------------VALIDO DIA----------------------------------
    if(document.getElementById('dia') != null){
        dia = document.getElementById('dia').value;
        if (dia == "0"){
            ok = false;
            spanClase.innerHTML = spanClase.innerHTML + 'Seleccione un día. ';
        }
    }

    //-------------------------------VALIDO DOCENTE----------------------------------
    if(document.getElementById('docente') != null){
        docente = document.getElementById('docente').value;
        if (docente == "0"){
            ok = false;
            spanClase.innerHTML = spanClase.innerHTML + 'Seleccione un docente. ';
        }
    }

    return ok;
}

function validarAgregarClase(){
    var isValid = validar();

    if (isValid){
        var formAgregar = document.forms['formAddClaseATaller'];
        formAgregar.submit();
    }
}

function validarEditarClase(){
    var isValid = validar();

    if (isValid){
        var formAgregar = document.forms['formAddClaseATaller'];
        formAgregar.submit();
    }
}

function cancelarEditarClase(){
    document.getElementById('inicio').value = "00:00";
    document.getElementById('fin').value = "23:59";
    document.getElementById('dia').value = "0";
    document.getElementById('claseEditar').value = "";
    document.getElementById('docente').value = "0";

    document.getElementById('nombre').innerHTML = 'Agregar clase';
    document.getElementById('inputAgregar').style.display = '';
    document.getElementById('inputEditar').style.display = 'none';
    document.getElementById('inputCancelar').style.display = 'none';
    document.getElementById('formAddClaseATaller').action="{{ url_for('add_clase') }}";
}
