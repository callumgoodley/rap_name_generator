from flask import Response, request
from application import app

def generate_rap_name(letter, number):
    number = int(float(number))
    adj = ['Young','Yung','Lil','Big','Sick','Ill','Wavy','DJ','D']
    noun =  ['Wizard','Fork','Mustard','Gambino','Strap','Chopper','Baby','Thumb','Poppa','Dripper','Purple','Clout','Icey','Nascar','Shooter','Xan','Emo','Dookey','God','Ram','Chapo','Bando','Jugg','Boii','Perc','Flossy','Dead','Door','Zilla','Lost','Savage','Coffin','Neck','Throat','Cautious','Beans','Rackz','$hawty','Ku$h']
    if letter == 'a' or letter == 'b' or letter == 'c':
        name = adj[0]
    elif letter == 'd' or letter == 'e' or letter == 'f':
        name = adj[1]
    elif letter == 'g' or letter == 'h' or letter == 'i':
        name = adj[2]
    elif letter == 'j' or letter == 'k' or letter == 'l':
        name = adj[3]
    elif letter == 'm' or letter == 'n' or letter == 'o':
        name = adj[4]
    elif letter == 'p' or letter == 'q' or letter == 'r':
        name = adj[5]
    elif letter == 's' or letter == 't' or letter == 'u':
        name = adj[6]
    elif letter == 'v' or letter == 'w' or letter == 'y':
        name = adj[7]
    else:
        name =adj[8]

    if number > 31 and number < 65:
        name += " " + noun[0]
    elif number > 65 and number < 75:
        name += " " + noun[1]
    elif number > 75 and number < 85:
        name += " " + noun[2]
    elif number > 75 and number < 85:
        name += " " + noun[3]
    elif number > 85 and number < 95:
        name += " " + noun[4]
    elif number > 95 and number < 105:
        name += " " + noun[5]
    elif number > 105 and number < 115:
        name += " " + noun[6]
    elif number > 115 and number < 125:
        name += " " + noun[7]
    elif number > 125 and number < 135 :
        name += " " + noun[8]
    else:
        name += " " + noun[9]
    
    return name

@app.route('/', methods = ['GET', 'POST'])
def home():



    code = request.data.decode('utf-8')
    
    code_list = code.split()
    
    letter = code_list[1]
    number = code_list[0]

    name = generate_rap_name(letter, number)
    


    return Response(name, mimetype='text/plain')
