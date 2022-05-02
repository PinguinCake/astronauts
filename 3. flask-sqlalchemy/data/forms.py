from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
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


class LoginForm(FlaskForm):
    """форма авторизации"""
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class WorksForm(FlaskForm):
    """форма добавления работ"""
    team_leader = StringField('ID of captain', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField("Collaborators' id", validators=[DataRequired()])
    is_finished = BooleanField('Is finished?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class WorksRedactionForm(FlaskForm):
    """форма редактирования работ"""
    team_leader = StringField('ID of captain', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField("Collaborators' id", validators=[DataRequired()])
    is_finished = BooleanField('Is finished?', validators=[DataRequired()])
    submit = SubmitField('Submit')