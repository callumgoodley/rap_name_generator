from flask_wtf import FlaskForm
from wtforms import SubmitField

class NameForm(FlaskForm):
    submit = SubmitField('get band name...')

