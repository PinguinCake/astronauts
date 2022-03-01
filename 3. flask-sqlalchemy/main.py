from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("Journal_works.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        return render_template('success.html', title='Успешно', data=form.login)
    return render_template('register.html', title='Регистрация', form=form)


def main():
    name_db = 'mars_explorer.db'
    db_session.global_init(f"db/{name_db}")
    app.run(port=5001)


if __name__ == '__main__':
    main()