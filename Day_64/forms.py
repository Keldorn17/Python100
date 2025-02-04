from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired, NumberRange


class EditForm(FlaskForm):

    rating = FloatField(label='Your Rating Out of 10 e.q. 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label='Your Review', validators=[DataRequired()])
    done = SubmitField(label='Done')


class AddForm(FlaskForm):

    title = StringField(label='Movie Title', validators=[DataRequired()])
    done = SubmitField(label='Add Movie')
