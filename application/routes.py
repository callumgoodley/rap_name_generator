from flask import render_template
from application import app
from application.forms import NameForm
import random

@app.route('/', methods = ['GET', 'POST'])
def home():

    form = NameForm()
    name = ''
    list1 = ["A", "B", "C"]
    list2 = ["1", "2", "3", "4"]

    random1 = random.choice(list1)
    random2 = random.choice(list2)

    code = random1 + random2

    if form.validate_on_submit():
        if code[0] == "A":
            name = "sharp shooter"
        elif code[0] == "B":
            name = "Crow city"
        elif code[0] == "C":
            name = "Jokers card"


    return render_template('home.html', title='Home', form = form,  code = code, name = name)
