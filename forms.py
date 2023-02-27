from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators 

def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message = 'El campo es requerido ')])
    amaterno = StringField('Amaterno', [mi_validacion])
    apaterno = StringField('Apaterno')
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('usuario',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])
    password = StringField('password',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])

class UseForm3(Form):
    Ingles = StringField('Ingles',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])
    Español = StringField('Español',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])
    RadIngles = RadioField('Ingles', [validators.DataRequired()])
    RadEspañol = RadioField('Español', [validators.DataRequired()])
