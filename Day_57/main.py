from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/blog')
def home():
    blog_data: list[dict] = fetch_data("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("index.html", data=blog_data)


@app.route('/post/<blog_id>')
def get_post(blog_id: str):
    blog_data: list[dict] = fetch_data("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("post.html", data=blog_data[int(blog_id) - 1])


def fetch_data(url: str) -> list[dict]:
    response: requests.Response = requests.get(url=url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
