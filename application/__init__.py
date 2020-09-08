from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy


from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('SOCIALAPP_URI')
app.config['SECRET_KEY']=getenv('SECRET_KEY')
bcrypt = Bcrypt(app)

db =  SQLAlchemy(app)
from application import routes
