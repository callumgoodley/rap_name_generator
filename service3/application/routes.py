from flask import render_template
from application import app
from application.forms import NameForm
import random
from random import randrange
@app.route('/', methods = ['GET', 'POST'])
def home():
    adj = ['Young','Yung','Lil','Big','Sick','Ill','Wavy','DJ','D']
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


        if unicode_letter == 'a' or unicode_letter == 'b' or unicode_letter == 'c':
            name = adj[0]
        elif unicode_letter == 'd' or unicode_letter == 'e' or unicode_letter == 'f':
            name = adj[1]
        elif unicode_letter == 'g' or unicode_letter == 'h' or unicode_letter == 'i':
            name = adj[2]
        elif unicode_letter == 'j' or unicode_letter == 'k' or unicode_letter == 'l':
            name = adj[3]
        elif unicode_letter == 'm' or unicode_letter == 'n' or unicode_letter == 'o':
            name = adj[4]
        elif unicode_letter == 'p' or unicode_letter == 'q' or unicode_letter == 'r':
            name = adj[5]
        elif unicode_letter == 's' or unicode_letter == 't' or unicode_letter == 'u':
            name = adj[6]
        elif unicode_letter == 'v' or unicode_letter == 'w' or unicode_letter == 'y':
            name = adj[7]
        else:
            name =adj[8]

        if unicode_num_first > 31 and unicode_num_first < 65:
            name += " " + noun[0]
        elif unicode_num_first > 65 and unicode_num_first < 75:
            name += " " + noun[1]
        elif unicode_num_first > 75 and unicode_num_first < 85:
            name += " " + noun[2]
        elif unicode_num_first > 75 and unicode_num_first < 85:
            name += " " + noun[3]
        elif unicode_num_first > 85 and unicode_num_first < 95:
            name += " " + noun[4]
        elif unicode_num_first > 95 and unicode_num_first < 105:
            name += " " + noun[5]
        elif unicode_num_first > 105 and unicode_num_first < 115:
            name += " " + noun[6]
        elif unicode_num_first > 115 and unicode_num_first < 125:
            name += " " + noun[7]
        elif unicode_num_first > 125 and unicode_num_first < 135 :
            name += " " + noun[8]
        else:
            name += " " + noun[9]


    return render_template('home.html', title='Home', form = form,  code = display_code, name = name)
