from flask import Response, request
from application import app

def generate_letter(name):
    unicode_sum_last = 0
    for letter in name:
        unicode_sum_last += ord(letter)
    unicode_num_last = int(unicode_sum_last/len(name))
    letter = chr(unicode_num_last)
    return letter

@app.route('/', methods = ['POST'])
def home():
    
    last_name = request.data.decode('UTF-8')
    
    letter = generate_letter(last_name)

    return Response(letter, mimetype='text/plain')
