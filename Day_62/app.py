from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask import url_for, redirect
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.q. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.q. 5:30PM', validators=[DataRequired()])
    __coffees = [(coffee, coffee) for coffee in ['☕' * i for i in range(1, 6)]]
    coffee_rating = SelectField("Coffee Rating", choices=__coffees, validators=[DataRequired()])
    __wifi = [(coffee, coffee) for coffee in ['💪' * i for i in range(1, 6)]]
    wifi_rating = SelectField("Wifi Strength Rating", choices=[('✘', '✘')] + __wifi, validators=[DataRequired()])
    __power = [(coffee, coffee) for coffee in ['🔌' * i for i in range(1, 6)]]
    __power.insert(0, ('✘', '✘'))
    power_rating = SelectField("Power Socket Availability", choices=__power, validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data
            ])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
