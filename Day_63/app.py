from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    title: Mapped[str] = mapped_column(unique=True, type_=String(250), nullable=False)
    author: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    rating: Mapped[float] = mapped_column(type_=Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        books = Books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(books)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit(book_id: int):
    result = db.session.execute(db.select(Books).where(Books.id == book_id))
    book = result.scalars().all()
    if request.method == 'POST':
        book_to_update = db.get_or_404(Books, book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book_data=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('book_id')
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

