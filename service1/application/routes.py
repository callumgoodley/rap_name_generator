from flask import render_template
from application import app, db
from application.forms import NameForm
from application.models import Users
import requests

@app.route('/', methods = ['GET', 'POST'])
def home():
    
    code_string = ''
    name = ''
    form = NameForm()
    
    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data

        unicode_num_first = requests.post('http://service2:5001', data=first_name)
        unicode_letter  = requests.post('http://service3:5002', data=last_name)
        
        code_string = unicode_num_first.text + " " + unicode_letter.text

        name = requests.post('http://service4:5003', data=code_string )

        postData = Users( first_name=first_name, last_name=last_name, rapper_name=name.text)
        db.session.add(postData)
        db.session.commit()

    return render_template('home.html', title='Home', form = form,  code = code_string, name = name)
