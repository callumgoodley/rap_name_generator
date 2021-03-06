from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + str(getenv('DB_USERNAME'))+ ':' + str(getenv('DB_PASSWORD')) + '@rapstack_mysql:3306/rapper-name-db'
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

db = SQLAlchemy(app)

from application import routes
