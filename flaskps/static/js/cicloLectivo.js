//Función que valida los campos del formulario.
function validarModificarCiclo(){
    var ok = true;
    fechaInicio = document.getElementById('fecha_ini').value;
    fechaFin = document.getElementById('fecha_fin').value;
    spanInicio = document.getElementById('spanInicio');
    spanFin = document.getElementById('spanFin');
    idSemestre = document.getElementById('idSemestre').value;
    spanSemestre = document.getElementById('spanSemestre');

    //Llamo a la función para limpiar los campos del formulario.
    limpiarCampos();

    //Valido que la fecha de inicio y fin no sean nulos.
    if(fechaInicio == '' & fechaFin == '')
    {
        ok = false;
        spanInicio.innerHTML = 'Ingrese una fecha inicio';
        spanFin.innerHTML = 'Ingrese una fecha fin';
    }
    else
    {
        //Valido que la fecha inicio no sea nulo.
        if(fechaInicio == ''){
            ok = false;
            spanInicio.innerHTML = 'Ingrese una fecha inicio';
        }
        else
        {
            //Valido que la fecha fin no sea nulo.
            if(fechaFin == ''){
                ok = false;
                spanFin.innerHTML = 'Ingrese una fecha fin';
            }
            else
            {
                //Valido que la fecha inicio no sea mayor a la fecha fin.
                if(fechaInicio > fechaFin)
                {
                    ok = false;
                    spanInicio.innerHTML = 'La fecha inicio no puede ser mayor a la fecha fin';
                }
            }
        }
    }

    //Valido que se haya seleccionado un semestre.
    if(idSemestre == "0"){
        ok = false;
        spanSemestre.innerHTML = 'Seleccione un semestre';
    }

    //Si ok es true hago submit.
    if (ok){
        var formAgregar = document.forms['formAgregar'];
        formAgregar.submit();
    }
}

//Función que limpia los campos del formulario.
function limpiarCampos(){
    spanInicio = document.getElementById('spanInicio');
    spanFin = document.getElementById('spanFin');
    spanSemestre = document.getElementById('spanSemestre');

    spanInicio.innerHTML = '';
    spanFin.innerHTML = '';
    spanSemestre.innerHTML = '';
}