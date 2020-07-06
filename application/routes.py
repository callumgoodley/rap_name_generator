from flask import render_template
from application import app
from application.forms import NameForm
import random

@app.route('/', methods = ['GET', 'POST'])
def home():
    adj = ['Young','Yung','Lil','Big','YBN','Sick','Ill','Wavy','DJ','D']
    noun =  ['Wizard','Fork','Mustard','Gambino','Strap','Chopper','Baby','Thumb','Poppa','Dripper','Purple','Clout','Icey','Nascar','Shooter','Xan','Emo','Dookey','God','Ram','Chapo','Bando','Jugg','Boii','Perc','Flossy','Dead','Door','Zilla','Lost','Savage','Coffin','Neck','Throat','Cautious','Beans','Rackz','$hawty','Ku$h']
    
    display_code = ''
    name = ''
    form = NameForm()
    
    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data

        unicode_sum_first = 0
        
        for letter in first_name:
            unicode_sum_first += ord(letter)
            
        unicode_sum_last = 0
        
        for letter in last_name:
            unicode_sum_last += ord(letter)
    
        unicode_num_first = int(unicode_sum_first/len(first_name))
        unicode_num_last = int(unicode_sum_last/len(last_name))
        unicode_letter = chr(unicode_num_last)
        
        display_code = "1: " + str(unicode_num_first) + " 2: " + unicode_letter


        if unicode_num_first > 0 and unicode_num_first < 50:
            name = "sharp shooter"
        elif unicode_num_first > 50 and unicode_num_first < 100:
            name = "Crow city"
        elif unicode_num_first > 100 and unicode_num_first < 300:
            name = "Jokers card"


    return render_template('home.html', title='Home', form = form,  code = display_code, name = name)
