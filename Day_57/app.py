from flask import Flask, render_template, request
from send_email import SendEmail
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


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'GET':
        return render_template("contact.html", title='Contact Me')
    else:
        # Sending email is disabled due to it's only a test project it's unnecessary to flood me with emails.
        # send_email: SendEmail = SendEmail(request.form)
        # send_email.send_email()
        return render_template("contact.html", title='Successfully sent message')


def fetch_data(url: str) -> list[dict]:
    response: requests.Response = requests.get(url=url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)  # flask --app app run --debug
