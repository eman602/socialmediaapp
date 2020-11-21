from application import db
from application.models import Users

db.drop_all()
#INSERT INTO users (username, first_name, second_name, email, password) 
db.create_all()
users= Users (username="emmanuelagy",first_name="Emmanuel", second_name="Agyapong", email="emmanuel.agy@hotmail.co.uk", password="hiya")

db.session.add(users)
db.session.commit()

