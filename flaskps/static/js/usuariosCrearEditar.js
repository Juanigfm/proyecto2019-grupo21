function validarAgregarUsuario(){
    var ok = true;
    
    // ------------------------VALIDO NOMBRE DE USUARIO-------------------------------
    usuario = document.getElementById('usuario').value;
    spanUsuario = document.getElementById('spanUsuario');
    if (usuario == ''){
         ok = false;
         spanUsuario.innerHTML = 'Ingrese un usuario';
    }else{
        if(!validateUsuario(usuario)){
            ok = false;
            spanUsuario.innerHTML = 'Solo puede contener caracteres alfanuméricos';
        }else{
            spanUsuario.innerHTML = '';
        }
    }
        
    // -------------------------------VALIDO EMAIL-----------------------------------
    email = document.getElementById('email').value;
    spanEmail = document.getElementById('spanEmail')
    if (email == ''){
        ok = false;
        spanEmail.innerHTML = 'Ingrese un email';
    }else{
        if(!validateEmail(email)){
            ok=false;
            spanEmail.innerHTML = 'Ingrese un email válido';
        }else{
            spanEmail.innerHTML = '';
        }
    }

    // -----------------------------VALIDO PASSWORD----------------------------------
    if (document.getElementById('password') != null) {
        password = document.getElementById('password').value;
        spanPassword = document.getElementById('spanPassword');
        if (password == '') {
            ok = false;
            spanPassword.innerHTML = 'Ingrese una contraseña';
        } else {
            if (password.length < 5 || password.length > 15) {
                ok = false;
                spanPassword.innerHTML = 'La contraseña debe tener entre 5 y 15 caracteres';
            } else {
                spanPassword.innerHTML = '';
            }
        }
    }
    
    
    //-------------------------------VALIDO NOMBRE------------------------------------
    firstName = document.getElementById('firstName').value;
    spanFirstName = document.getElementById('spanFirstName');
    if (firstName == ''){
         ok = false;
         spanFirstName.innerHTML = 'Ingrese un nombre';
    }else{
        spanFirstName.innerHTML = '';
    }

    //-------------------------------VALIDO APELLIDO----------------------------------
    lastName = document.getElementById('lastName').value;
    spanLastName = document.getElementById('spanLastName');
    if (lastName == ''){
         ok = false;
         spanLastName.innerHTML = 'Ingrese un apellido';
    }else{
        spanLastName.innerHTML = '';
    }

    //-------------------------------VALIDO ROLES----------------------------------
    if(document.getElementsByName('roles').length > 0){
        var checkboxes = document.getElementsByName('roles');
        var checkboxesChecked = [];
        spanRoles = document.getElementById('spanRoles');
        for (var i=0; i<checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                checkboxesChecked.push(checkboxes[i]);
            }
        }
        if(checkboxesChecked.length == 0){
            ok = false;
            spanRoles.innerHTML = 'Seleccione al menos un rol';
        }else{
            spanRoles.innerHTML='';
        }
    }

    if (ok){
        var formAgregar = document.forms['formAgregar'];
        formAgregar.submit();
    }
}

function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function validateUsuario(usuario) {
    var re = /^[a-zA-Z0-9]*$/;
    return re.test(usuario);
}
