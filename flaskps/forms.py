from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import validators 

class LoginForm(Form):
    email= EmailField('',
    [
        validators.Required(message = 'Ingrese un nombre de usuario'),
    ])
    
    password= PasswordField('',
    [
        validators.Required(message = 'Ingrese una contraseña')
    ])

class CreateUserForm(Form):
    usuario= StringField('usuario',
    [
        validators.Required(message = 'Ingrese un usuario')
    ])
    
    password= PasswordField('password',
    [
        validators.Required(message = 'Ingrese una contraseña'),
        validators.length(min=5, max=15, message='La contraseña debe tener entre 5 y 15 caracteres')
    ])

    email= EmailField('email',
    [
        validators.Required(message = 'Ingrese un email'),
        validators.Email(message = 'Ingrese un email válido')
    ])

    firstName= StringField('firstName',
    [
        validators.Required(message = 'Ingrese un nombre')
    ])

    lastName= StringField('lastName',
    [
        validators.Required(message = 'Ingrese un apellido')
    ])
