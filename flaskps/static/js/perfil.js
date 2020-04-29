function validatePasswordChange(){
    var ok = true;
    
    // ------------------------VALIDO NOMBRE DE USUARIO-------------------------------
    newpassword = document.getElementById('newpassword').value;
    newpasswordcopy = document.getElementById('newpasswordcopy').value;
    spanNewPasswordCopy = document.getElementById('spanNewPasswordCopy');

    if (newpassword != newpasswordcopy){
        ok = false;
        spanNewPasswordCopy.innerHTML = 'No coincide con la nueva contraseña.';
    }else{
        spanNewPasswordCopy.innerHTML = '';
    }    
   
    if (ok){
        var formChangePassword = document.forms['formChangePassword'];
        formChangePassword.submit();
    }

        
}