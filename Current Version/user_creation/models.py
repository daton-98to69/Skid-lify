from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))  # 10000 is the character limit
    # date = db.Column(db.DateTime(timezone=True), default=func.now)   #### Check on this
    # User_id calls User class and takes id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # For foreignkey ---> use lower case
    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Uniqure identifier
    # unique makes user that no two user has same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    notes = db.relationship('Note')
