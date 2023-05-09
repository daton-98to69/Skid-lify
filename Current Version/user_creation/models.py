from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))  # 10000 is the character limit
#     # date = db.Column(db.DateTime(timezone=True), default=func.now)   #### Check on this
#     # User_id calls User class and takes id
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     # For foreignkey ---> use lower case

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Uniqure identifier
    # unique makes user that no two user has same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    # notes = db.relationship('Note')
    user_info = db.relationship('UserInfo', backref = 'user')

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjects = db.Column(db.String(150))
    major = db.Column(db.String(150))
    quotes = db.Column(db.String(150))
    clubs = db.Column(db.String(150))
    profile_pic = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

class CoffeeTalks_list(db.Model):
    event_name = db.Column(db.String(150),primary_key=True, unique=True)
    time_event = db.Column(db.Integer())
    description = db.Column(db.String(500))
    events_picture = db.Column(db.String(300))



