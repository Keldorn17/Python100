# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import Integer, String, Float
#
# app = Flask(__name__)
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
#
# db = SQLAlchemy(model_class=Base)
# db.init_app(app)
#
#
# class Books(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, type_=Integer)
#     title: Mapped[str] = mapped_column(unique=True, type_=String(250), nullable=False)
#     author: Mapped[str] = mapped_column(type_=String(250), nullable=False)
#     rating: Mapped[float] = mapped_column(type_=Float, nullable=False)
#
#     def __repr__(self):
#         return f'<Book {self.title}>'
#
#
# with app.app_context():
#     db.create_all()
#
# with app.app_context():
#     books = Books(
#         title='Harry Potter',
#         author='J. K. Rowling',
#         rating=9.3
#     )
#     db.session.add(books)
#     db.session.commit()
#
#
# @app.route('/')
# def home():
#     return 'bello world'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

