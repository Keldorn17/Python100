from flask import Flask
import random

app = Flask(__name__)
number_to_guess: int = random.randint(0, 9)


@app.route('/')
def hello_world():  # put application's code here
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxscHBvYm53MDZmcDJ4MDRlZzkwZ2dkcWt1aWJ2eXZxd2V3cnA0MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uSeXREed0RSfcTseo0/giphy.gif">')


@app.route('/<int:number>')
def number_guess(number):
    if number == number_to_guess:
        return ('<h1 style="color:green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    return ('<h1 style="color:purple">Too high, try again!!</h1>'
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
            if number > number_to_guess else
            '<h1 style="color:red">Too low, try again!</h1>'
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
            )


if __name__ == '__main__':
    app.run(debug=True)
