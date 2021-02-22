from models import Pet, db
from app import app

db.drop_all()
db.create_all()

smokey = Pet(name="Smokey", species="Cat", photo_url="https://cataas.com/cat", age=13, notes="He doesn't like strangers.", available=True)
polly = Pet(name="Polly", species="Cat", photo_url="https://cataas.com/cat", age=6, notes="Acts like a dog", available=True)
fiona = Pet(name="Fiona", species="Cat", photo_url="https://cataas.com/cat", age=9, notes="Sticks to herself", available=False)
db.session.add(smokey)
db.session.add(polly)
db.session.add(fiona)
db.session.commit()