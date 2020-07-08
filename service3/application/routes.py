from flask import Response, request
from application import app
@app.route('/', methods = ['POST'])

def generate_letter(name):

    unicode_sum_last = 0
    
    for letter in name:
        unicode_sum_last += ord(letter)
    
    unicode_num_last = int(unicode_sum_last/len(name))
    letter = chr(unicode_num_last)

    return letter

def home():
    
    last_name = request.data.decode('UTF-8')
    
    letter = generate_letter(last_name)

    return Response(letter, mimetype='text/plain')
