from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index2.html", rn=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name: str):
    gender: str = fetch_data(f"https://api.genderize.io?name={name}")["gender"]
    age: int = int(fetch_data(f"https://api.agify.io/?name={name}")["age"])
    return render_template("guess.html", name=name.title(), gender=gender, age=age)


@app.route('/blog')
def get_blog():
    blog_data: dict = fetch_data("https://api.npoint.io/c790b4d5cab58020d391")
    current_year = datetime.datetime.now().year
    return render_template("blog.html", posts=blog_data, year=current_year)


def fetch_data(url: str) -> dict:
    response: requests.Response = requests.get(url=url)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    app.run()
