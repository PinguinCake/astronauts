from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    """форма регистрации"""
    login = StringField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname')
    name = StringField('Name')
    age = StringField('Age')
    position = StringField('Position')
    speciality = StringField('Speciality')
    address = StringField('Address')
    submit = SubmitField('Submit')
