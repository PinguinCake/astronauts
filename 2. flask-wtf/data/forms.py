from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Задача Двойная защита"""
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id астронавта', validators=[DataRequired()])
    password_cap = PasswordField('Пароль астронавта', validators=[DataRequired()])
    enter = SubmitField('Доступ')