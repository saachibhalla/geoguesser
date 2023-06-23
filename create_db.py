from GeoGuesser import create_app, db, bcrypt

from GeoGuesser.models import User
app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

user = User(
    firstname = 'Saachi',
    lastname = 'Bhalla',
    alias = "Person",
    email = "saachi.bhalla@surreyschools.ca",
    password = bcrypt.generate_password_hash('password'),
    
)

db.session.add(user)
db.session.commit()