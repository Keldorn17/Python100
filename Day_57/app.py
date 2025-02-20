from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from send_email import SendEmail
from forms import MakePost, RegisterForm, LoginForm, CommentForm
from database import db, Database, BlogPost, User, Comment
from dotenv import load_dotenv
import os


load_dotenv('.env')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
# python -c 'import secrets; print(secrets.token_hex())'
ckeditor = CKEditor()
ckeditor.init_app(app)
database = Database(app, 'posts.db')
Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)
gravatar = Gravatar(app,
                    size=50,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.get_id() != '1':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=result,
                           logged_in=current_user.is_authenticated, user_id=current_user.get_id())


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id: int):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You need to login or register to comment.')
            return redirect(url_for('login'))
        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, form=comment_form,
                           logged_in=current_user.is_authenticated, user_id=current_user.get_id())


@app.route('/new-post', methods=['GET', 'POST'])
@admin_only
def add_new_post():
    post_form = MakePost()
    if post_form.validate_on_submit():
        today = date.today()
        post = BlogPost(
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            author_id=current_user.get_id(),
            img_url=request.form.get('img_url'),
            body=request.form.get('body'),
            date=today.strftime('%B %d, %Y')
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=post_form, is_edit=False, logged_in=current_user.is_authenticated)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@admin_only
def edit_post(post_id: int):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = MakePost(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template('make-post.html', form=edit_form, is_edit=True, logged_in=current_user.is_authenticated)


@app.route('/delete/<int:post_id>')
@admin_only
def delete_post(post_id: int):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route('/about')
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Sending email is disabled due to prevent spamming emails.
        # send_email: SendEmail = SendEmail(request.form)
        # send_email.send_email()
        return render_template("contact.html", msg_sent=True, logged_in=current_user.is_authenticated)
    return render_template("contact.html", msg_sent=False, logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if result is not None:
            flash('You\'ve already signed up with that email, log in instead.')
            return redirect(url_for('login'))
        hashed_and_salted_password = generate_password_hash(request.form.get('password'), salt_length=16)
        user = User(
            email=request.form.get('email'),
            password=hashed_and_salted_password,
            name=request.form.get('name')
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=register_form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        print(user)
        if user is None:
            flash('That email does not exist, please try again.')
        elif check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('get_all_posts'))
        else:
            flash('Password incorrect, please try again,')
    return render_template("login.html", form=login_form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=False)  # flask --app app run --debug
