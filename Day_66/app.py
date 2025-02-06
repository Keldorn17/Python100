from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from dataclasses import dataclass
import random
from werkzeug.exceptions import NotFound

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
@dataclass
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random_route():
    max_index = db.session.execute(db.select(func.max(Cafe.id)))
    while True:
        random_index = random.randint(1, int(max_index.scalar()))
        random_cafe = db.get_or_404(Cafe, random_index)
        if random_cafe:
            break
    return jsonify({'cafe': random_cafe})  # https://tedboy.github.io/flask/generated/flask.jsonify.html


@app.route('/all', methods=['GET'])
def get_all():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify({'cafe': result})


@app.route('/search', methods=['GET'])
def get_search():
    loc = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if not result:
        return jsonify({'error': {'Not Found': "Sorry, we don't have a cafe at that location."}})
    return jsonify({'cafe': result})


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def post_add():
    if not request.form:
        return jsonify({'response': {'error': 'No data provided.'}})
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({'response': {'success': 'Successfully added the new cafe.'}})


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id: int):
    new_price = request.args.get('new_price')
    result = db.session.get(Cafe, cafe_id)  # db.get_or_404(Cafe, cafe_id) will automatically return 404 if not found
    if not result:
        return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'}), 404
    result.coffee_price = new_price
    db.session.commit()
    return jsonify(response={'success': 'Successfully updated the price.'}), 200


# HTTP DELETE - Delete Record
@app.route('/delete/<int:cafe_id>', methods=['DELETE'])
def delete_item(cafe_id: int):
    api_key = request.headers.get('x-api-key')
    print(api_key)
    if api_key != 'TopSecretAPIKey':
        return jsonify(error='Sorry, that\'s not allowed. Make sure you have the correct api_key.'), 403
    try:
        result = db.get_or_404(Cafe, cafe_id)
        db.session.delete(result)
        db.session.commit()
    except NotFound:
        return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'}), 404
    return jsonify(response={'success': 'Successfully deleted the cafe from the database.'}), 200


if __name__ == '__main__':
    app.run(debug=True)
