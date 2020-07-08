from flask import Response, request
from application import app

@app.route('/', methods = ['POST'])
def home():
    
    first_name = request.data.decode('utf-8')

    unicode_sum = 0
        
    for letter in first_name:
        unicode_sum += ord(letter)
    
    unicode_num_first = unicode_sum/len(first_name)
    int_num = int(unicode_num_first)
    number = str(unicode_num_first)

    return Response(number, mimetype='text/plain')
