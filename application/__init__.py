from flask import Flask
from os import getenv
import os
#from flask_sqlalchemy import SQLALchemy
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] ="1245"
from application import routes
