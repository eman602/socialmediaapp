from flask import Flask
import os
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=str(os.getenv('SOCIALAPP_URI'))
app.config['SECRET_KEY']=getenv('SECRET_KEY')

bcrypt = Bcrypt(app)
db =  SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from application import routes
