from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Film(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(255), nullable=True)
    img_url: Mapped[str] = mapped_column(String(255), nullable=False)


class Database:

    def __init__(self, app: Flask):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///films.db"
        db.init_app(app)

        with app.app_context():
            db.create_all()

