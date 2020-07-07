from flask import Response, request
from application import app

@app.route('/', methods = ['POST'])
def home():
    
    first_name = request.data.decode('utf-8')

    unicode_sum = 0
        
    for letter in first_name:
        unicode_sum += ord(letter)
    
    unicode_num_first = str(unicode_sum_first/len(first_name))

    return Response(unicode_num_first, mimetype='text/plain')
