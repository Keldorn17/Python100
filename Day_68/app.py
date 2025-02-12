from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '21137fcae5e6640e409ca71dcba1aeb3663316b421fbb78d22284229b2003ae6'
# python -c 'import secrets; print(secrets.token_hex())'
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if result is not None:
            flash('You\'ve already signed up with that email, log in instead.')
            return redirect(url_for('login'))
        hash_and_salted_password = generate_password_hash(request.form.get('password'), salt_length=16)
        user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name')
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user is None:
            flash('That email does not exist, please try again.')
            return render_template("login.html", logged_in=current_user.is_authenticated)
        if check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Password incorrect, please try again,')
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods=['GET'])
@login_required
def download():
    return send_from_directory(
        'static', 'files/cheat_sheet.pdf'
    )  # The file will be auto downloaded, if 'as_attachment=True' is added as a keyword argument


if __name__ == "__main__":
    app.run(debug=True)
