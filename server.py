from flask import Flask, url_for, request, render_template, redirect
from flask_login import login_user, LoginManager, logout_user, login_required

from data import db_session, fan_api
from data.fan import Fan
from data.users import User
from forms.reg import LoginForm
from forms.user import RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

s = ''
d = []
DB_NAME = 'rain'

settings = {'user_name': 'Вася',
            }


@app.route('/')
@app.route('/home')
def home():
    db_sess = db_session.create_session()
    news = db_sess.query(Fan)
    return render_template("home.html", news=news)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    d = []
    if request.method == 'GET':
        return render_template("edit.html", title="title")
    elif request.method == 'POST':
        name = request.form['author']
        s = request.form['about']
        v = request.form['title']
        w = request.form['fandom']
        s = s.replace("<", "(")
        s = s.replace(">", ")")
        db_sess = db_session.create_session()
        au_id = db_sess.query(User).filter(User.name == name).first().id
        print(d, au_id, v, w)
        db_sess = db_session.create_session()
        fan = Fan()
        fan.title = v
        fan.content = s
        fan.fandom = w
        fan.user_id = au_id
        db_sess.add(fan)
        db_sess.commit()
        with open('text.txt', "w", encoding="UTF-8") as e:
            e.write(s)
        return redirect("/home")


@app.route('/book/<id>')
def book(id):
    d = []
    db_sess = db_session.create_session()
    fan = db_sess.query(Fan).get(id).content
    for i in fan:
        d.append(i)
    d = "".join(d)
    d = d.split("\n")
    return render_template("book.html", text=d)


@app.route('/bot')
def bot():
    return render_template("bot.html")


# @app.errorhandler(404)
# def not_found(error):
#     return render_template()
#
#
# @app.errorhandler(400)
# def bad_request(_):
#     return render_template()


@app.route('/enter', methods=['POST', 'GET'])
def enter():
    if request.method == 'POST':
        f = request.files['file']
        settings["avatar_file"] = f.filename
        if settings['avatar_file'][settings['avatar_file'].rfind(".") + 1:] == "mp4":
            f.save(f'static/video/{f.filename}')
        elif settings['avatar_file'][settings['avatar_file'].rfind(".") + 1:] == "mp3":
            f.save(f'static/music/{f.filename}')
        else:
            f.save(f'static/img/{f.filename}')

    params = {'title': 'Выбор аватара!!!'}
    if 'avatar_file' in settings:
        if settings['avatar_file'][settings['avatar_file'].rfind(".") + 1:] == "mp4":
            params['avatar'] = url_for('static', filename=f"video/{settings['avatar_file']}")
        elif settings['avatar_file'][settings['avatar_file'].rfind(".") + 1:] == "mp3":
            params['avatar'] = url_for('static', filename=f"music/{settings['avatar_file']}")
        else:
            params['avatar'] = url_for('static', filename=f"img/{settings['avatar_file']}")
    return render_template("enter.html", **params)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            password=form.password.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            print('hi')
            return redirect("/home")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init(f"db/{DB_NAME}.db")
    app.register_blueprint(fan_api.blueprint)

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
