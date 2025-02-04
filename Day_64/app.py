from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from sqlalchemy import desc
from database import db, Database, Film
from forms import EditForm, AddForm
from dotenv import load_dotenv
import os
from utils import fetch_data


load_dotenv('.env')
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
database = Database(app)


@app.route('/')
def home():
    result = db.session.execute(db.select(Film).order_by(desc(Film.rating)))  # type: ignore
    all_films = result.scalars().all()
    # # Sort films by rating in descending order
    # all_films.sort(key=lambda film: film.rating, reverse=True)
    for i, film in enumerate(all_films):
        film.ranking = i + 1
    db.session.commit()
    return render_template("index.html", films=all_films)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    film_id = request.args.get('id')
    if edit_form.validate_on_submit():
        film_update = db.get_or_404(Film, film_id)
        film_update.rating = request.form.get('rating')
        film_update.review = request.form.get('review')
        db.session.add(film_update)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form)


@app.route('/delete')
def delete():
    film_id = request.args.get('id')
    delete_film = db.get_or_404(Film, film_id)
    db.session.delete(delete_film)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add_film():
    add_form = AddForm()
    if request.method == 'POST':
        film_title = request.form.get('title')
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {os.getenv('API_READ_ACCESS_TOKEN')}'
        }
        params = {
            'query': film_title
        }
        films = fetch_data(url='https://api.themoviedb.org/3/search/movie', headers=headers, params=params)
        return render_template('select.html', films=films)
    return render_template('add.html', form=add_form)


@app.route('/find')
def find():
    film_id = request.args.get('id')
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {os.getenv('API_READ_ACCESS_TOKEN')}'
    }
    film_data = fetch_data(f'https://api.themoviedb.org/3/movie/{film_id}', headers=headers)
    film = Film(
        title=film_data['title'],
        year=film_data['release_date'].split("-")[0],
        description=film_data['overview'],
        img_url=f'https://image.tmdb.org/t/p/w500{film_data['poster_path']}'
    )
    db.session.add(film)
    db.session.commit()
    return redirect(url_for('edit', id=film.id))


if __name__ == '__main__':
    app.run(debug=True)
