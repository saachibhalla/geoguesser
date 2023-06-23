#import

from .import db, login_manager
from flask import current_app as app
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    User.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key= True)
    firstname = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50))
    alias = db.Column(db.String(50), nullable = False, unique = True) 
    password = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(128), nullable = False, unique = True)
    avatars = db.Column(db.String(40), nullable = False, default = 'default.png')
    account_created = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow)
    active = db.Column(db.Boolean, default = True, nullable = False)

    def __repr__(self):
        return f'{self.firstname} {self.lastname} - {self.email}'

