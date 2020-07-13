from flask import Response, request
from application import app

def generate_rap_name(letter, number):
    number = int(float(number))
    adj = ['Young','Yung','Lil','Big','Sick','Ill','Wavy','DJ','D']
    noun =  ['Wizard','Fork','Mustard','Gambino','Strap','Chopper','Baby','Thumb','Poppa','Dripper','Purple','Clout','Icey','Nascar','Shooter','Xan','Emo','Dookey','God','Ram','Chapo','Bando','Jugg','Boii','Perc','Flossy','Dead','Door','Zilla','Lost','Savage','Coffin','Neck','Throat','Cautious','Beans','Rackz','$hawty','Ku$h']
    if letter == 'a' or letter == 'b' or letter == 'c' or letter == 'A' or letter == 'B' or letter == 'C':
        name = adj[0]
    elif letter == 'd' or letter == 'e' or letter == 'f' or letter == 'D' or letter == 'E' or letter == 'F':
        name = adj[1]
    elif letter == 'g' or letter == 'h' or letter == 'i' or letter == 'G' or letter == 'H' or letter == 'I':
        name = adj[2]
    elif letter == 'j' or letter == 'k' or letter == 'l' or letter == 'J' or letter == 'K' or letter == 'L':
        name = adj[3]
    elif letter == 'm' or letter == 'n' or letter == 'o' or letter == 'M' or letter == 'N' or letter == 'O':
        name = adj[4]
    elif letter == 'p' or letter == 'q' or letter == 'r' or letter == 'P' or letter == 'Q' or letter == 'R':
        name = adj[5]
    elif letter == 's' or letter == 't' or letter == 'u' or letter == 'S' or letter == 'T' or letter == 'U':
        name = adj[6]
    elif letter == 'v' or letter == 'w' or letter == 'x' or letter == 'V' or letter == 'W' or letter == 'X':
        name = adj[7]
    else:
        name =adj[8]

    if number > 31 and number < 65:
        name += " " + noun[0]
    elif number > 65 and number < 75:
        name += " " + noun[1]
    elif number > 75 and number < 85:
        name += " " + noun[2]
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
    
    split_code = code.split()
    
    letter = split_code[1]
    number = split_code[0]

    name = generate_rap_name(letter, number)
    


    return Response(name, mimetype='text/plain')
