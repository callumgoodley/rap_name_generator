from flask import Response, request
from application import app

@app.route('/', methods = ['POST'])

def generate_number(name):
        unicode_sum = 0

        for letter in name:
            unicode_sum += ord(letter)

        unicode_num_first = unicode_sum/len(name)
        int_num = int(unicode_num_first)
        number = str(unicode_num_first)

        return number

def home():

    first_name = request.data.decode('utf-8')

    number = generate_num(first_name)

    return Response(number, mimetype='text/plain')
