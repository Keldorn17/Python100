from flask import Flask, render_template
import requests

POST_API_ENDPOINT: str = "https://api.npoint.io/674f5423f73deab1e9a7"


app = Flask(__name__)


@app.route('/')
def home():
    blog_data: list[dict] = fetch_data(POST_API_ENDPOINT)
    return render_template("index.html", data=blog_data)


@app.route('/post/<blog_id>')
def get_post(blog_id: str):
    blog_data: list[dict] = fetch_data(POST_API_ENDPOINT)
    return render_template("post.html", data=blog_data[int(blog_id) - 1])


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


def fetch_data(url: str) -> list[dict]:
    response: requests.Response = requests.get(url=url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
