from flask import Flask, render_template
from forms import LoginForm
from flask_bootstrap import Bootstrap5

# python -m pip install -r requirements.txt |-> To install all the requirements.
# pip freeze > requirements.txt
app = Flask(__name__)
app.secret_key = '35ddf26bcc57d55324f9984cbfcb2f599804a57b1d956f86208db2eaabc50ac3'
bootstrap = Bootstrap5(app)


@app.route('/')
def home() -> str:
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    login_form = LoginForm()
    template = render_template('login.html', form=login_form)
    if login_form.validate_on_submit():
        admin_credentials: dict[str, str] = {
            'email': 'admin@email.com',
            'password': '12345678'
        }
        if (login_form.email.data == admin_credentials['email'] and
                login_form.password.data == admin_credentials['password']):
            template = render_template('success.html')
        else:
            template = render_template('denied.html')
    return template


if __name__ == '__main__':
    app.run(debug=True)
