from flask import Flask, render_template, request, redirect
from data.forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("base.html", title="Главная")


@app.route('/answer')
@app.route("/auto_answer")
def auto_answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе'
    param['ready'] = 'True'
    return render_template('auto_answer.html', data=param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('success.html', title='Успешно', data=form.id_astr)
    return render_template('login.html', title='Авторизация', form=form)


def main():
    app.run(port=5001)


if __name__ == '__main__':
    main()
