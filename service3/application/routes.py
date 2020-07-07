from flask import Response, request
from application import app
@app.route('/', methods = ['POST'])
def home():
    
    last_name = request.data.decode('UTF-8')
    unicode_sum_last = 0
    
    for letter in last_name:
        unicode_sum_last += ord(letter)
        
    unicode_num_last = int(unicode_sum_last/len(last_name))
    unicode_letter = chr(unicode_num_last)
    letter = str(unicode_letter)    

    return Response(letter, mimetype='text/plain')
