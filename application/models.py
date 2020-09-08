from application import db
from sqlalchemy.orm import relationship

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ''.join(['User:',self.username, ' ', self.first_name, ' ', self.second_name,
        '\r\n', 'Title: ', self.email, '\r\n', self.password
        ])



    