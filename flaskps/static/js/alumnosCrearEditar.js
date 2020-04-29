function validarAgregarAlumno(){
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

    //-------------------------------VALIDO APELLIDO----------------------------------
    apellido = document.getElementById('apellido').value;
    spanApellido = document.getElementById('spanApellido');
    if (apellido == ''){
         ok = false;
         spanApellido.innerHTML = 'Ingrese un apellido';
    }else{
        spanApellido.innerHTML = '';
    }

    //------------------------------VALIDO FECHA NACIMIENTO---------------------------
    
    fecha_nac = document.getElementById('fecha_nac').value;
    spanFechaNac = document.getElementById('spanFechaNac');

    if (fecha_nac == '' || new Date(fecha_nac) > new Date()){
        ok = false;
        spanFechaNac.innerHTML = 'Ingrese una fecha menor a la actual';
    }else{
        spanFechaNac.innerHTML = '';
    }

    //------------------------------VALIDO DOMICILIO------------------------
    domicilio = document.getElementById('domicilio').value;
    spanDomicilio = document.getElementById('spanDomicilio');
    if (domicilio == ''){
         ok = false;
         spanDomicilio.innerHTML = 'Ingrese un domicilio';
    }else{
        spanDomicilio.innerHTML = '';
    }

    //------------------------------VALIDO BARRIO------------------------
    if(document.getElementById('barrios') != null){
        barrio = document.getElementById('barrios').value;
        spanBarrios = document.getElementById('spanBarrios');
        if (barrio == "0"){
             ok = false;
             spanBarrios.innerHTML = 'Seleccione un barrio';
        }else{
            spanBarrios.innerHTML = '';
        }
    }

    //------------------------------VALIDO GENERO------------------------
    // if(document.getElementById('generos')!= null){
        genero = document.getElementById('generos').value;
        spanGeneros = document.getElementById('spanGeneros');
        if (genero == "0"){
             ok = false;
             spanGeneros.innerHTML = 'Seleccione un género';
        }else{
            spanGeneros.innerHTML = '';
        }
    // }

    //------------------------------VALIDO TIPO DOCUMENTO------------------------
    tipoDocumento = document.getElementById('tiposDocumento').value;
    spanTiposDocumento = document.getElementById('spanTiposDocumento');
    if (tipoDocumento == "0"){
         ok = false;
         spanTiposDocumento.innerHTML = 'Seleccione un tipo de documento';
    }else{
        spanTiposDocumento.innerHTML = '';
    }

    //------------------------------VALIDO NUMER DOC------------------------
    numero = document.getElementById('numero').value;
    spanNumero = document.getElementById('spanNumero');
    if (numero == ''){
         ok = false;
         spanNumero.innerHTML = 'Ingrese un número de documento';
    }else{
        if (!(/^\d+$/.test(numero))){
            ok = false;
            spanNumero.innerHTML = 'Solo se permiten números';
        }
        else{
            spanNumero.innerHTML = '';
        }
    }
    

    //------------------------------VALIDO RESPONSABLE------------------------
    if(document.getElementById('responsables') != null){
        responsable = document.getElementById('responsables').value;
        spanResponsables = document.getElementById('spanResponsables');
        if (responsable == "0"){
             ok = false;
             spanResponsables.innerHTML = 'Seleccione un responsable a cargo';
        }else{
            spanResponsables.innerHTML = '';
        }
    }

    //------------------------------VALIDO ESCUELA------------------------
    if(document.getElementById('escuelas') != null){
        escuela = document.getElementById('escuelas').value;
        spanEscuelas = document.getElementById('spanEscuelas');
        if (escuela == "0"){
            ok = false;
            spanEscuelas.innerHTML = 'Seleccione una escuela';
        }else{
            spanEscuelas.innerHTML = '';
        }
    }

    //------------------------------VALIDO NIVEL------------------------
    if(document.getElementById('niveles') != null){
        nivel = document.getElementById('niveles').value;
        spanNiveles = document.getElementById('spanNiveles');
        if (nivel == "0"){
            ok = false;
            spanNiveles.innerHTML = 'Seleccione un nivel';
        }else{
            spanNiveles.innerHTML = '';
        }
    }

    if (ok){
        var formAgregar = document.forms['formAgregar'];
        formAgregar.submit();
    }
}

// function validateEmail(email) {
//     var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     return re.test(email);
// }

// function validateUsuario(usuario) {
//     var re = /^[a-zA-Z0-9]*$/;
//     return re.test(usuario);
// }
