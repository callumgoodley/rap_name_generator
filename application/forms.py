from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    first_name  = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    last_name  = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    submit = SubmitField('get rapper name...')

