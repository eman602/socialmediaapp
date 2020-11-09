from application import db
from sqlalchemy.orm import relationship
from application import login_manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(['User:',self.username, ' ', self.first_name, ' ', self.second_name,
        '\r\n', 'Title: ', self.email, '\r\n', self.password
        ])


@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))
    