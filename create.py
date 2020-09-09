from application import db
from application.models import Users

db.drop_all()
#INSERT INTO users (username, first_name, second_name, email, password) 
db.create_all()
users= Users (username="emmanuelagy",first_name="Emmanuel", second_name="Agyapong", email="emmanuel.agy@hotmail.co.uk", password="hiya")
users2= Users (username="mercyagy",first_name="Mercy", second_name="Agyapong", email="mercy.agy@hotmail.co.uk", password="monday")
users3= Users (username="marthaagy",first_name="Martha", second_name="Agyapong", email="martha.agy@hotmail.co.uk", password="tuesday")
users4= Users (username="sarahagy",first_name="Sarah", second_name="Agyapong", email="sarah.agy@hotmail.co.uk", password="thursday")
users5= Users (username="isaacagy",first_name="Isaac", second_name="Agyapong", email="isaac.agy@hotmail.co.uk", password="friday")
db.session.add(users)
db.session.add(users2)
db.session.add(users3)
db.session.add(users4)
db.session.add(users5)
db.session.commit()

