from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from datetime import date
from send_email import SendEmail
from forms import MakePost
from database import db, Database, BlogPost

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor()
ckeditor.init_app(app)
database = Database(app, 'posts.db')
Bootstrap5(app)


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=result)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    post_form = MakePost()
    if post_form.validate_on_submit():
        today = date.today()
        post = BlogPost(
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            author=request.form.get('author'),
            img_url=request.form.get('img_url'),
            body=request.form.get('body'),
            date=today.strftime('%B %d, %Y')
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=post_form, is_edit=False)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
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
    return render_template('make-post.html', form=edit_form, is_edit=True)


@app.route('/delete/<int:post_id>')
def delete_post(post_id: int):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Sending email is disabled due to prevent spamming emails.
        # send_email: SendEmail = SendEmail(request.form)
        # send_email.send_email()
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)  # flask --app app run --debug
