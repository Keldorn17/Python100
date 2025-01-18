from flask import Flask
from functools import wraps

app = Flask(__name__)


def add_tag(format_tag: str):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return f'<{format_tag}>{function()}</{format_tag}>'
        return wrapper
    return decorator


def make_bold(function):
    @wraps(function)
    def inner(*args, **kwargs):
        return f'<b>{function()}</b>'
    return inner


@app.route('/')
def hello_world():  # put application's code here
    return ('<h1 style="text-align:center">Hello World!</h1>'
            '<p>This is a paragraph.</p>')


@app.route('/bye')
@make_bold
@add_tag('u')
def bye():
    return 'Bye'


@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."


if __name__ == '__main__':
    app.run(debug=True)
