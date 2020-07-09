from werkzeug.security import (
    gen_salt,
    generate_password_hash,
    check_password_hash
)
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from hashlib import md5
from flask_json import jsonify


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#base model, also controls access level (Admin/Staff/User)
#Admin has total control, staff has same access except cannot delete admin,
#accounts.
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO add role levels
    users = db.relationship('User', backref='role')

#table for Users. Holds ID, Username, Email, Created on date.
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    createdOn = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    password_hash = db.Column(db.String(256))
    about_me = db.Column(db.String(140))
    last_online = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    user_belts = db.relationship('UserBelt', backref='user')
    locksForSale = db.relationship('LocksForSale', backref='user')
    locksOnLoan = db.relationship('LocksOnLoan', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #TODO check if this can be removed post development,
    # feels really...vulnerable to leave this here.
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size
        )
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserBelt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    belt_name = db.Column(db.String(16), index=True)
    UsrBelt = db.Column(db.Integer, db.ForeignKey('user.id'))

class LocksForSale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lockname = db.Column(db.String(64), index=True)
    ownedBy = db.Column(db.String(64), index=True)
    LfS = db.Column(db.Integer, db.ForeignKey('user.id'))

class LocksOnLoan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lockname = db.Column(db.String(64), index=True)
    ownedBy = db.Column(db.String(64), index=True)
    loanedTo = db.Column(db.String(64), index=True)
    LoL = db.Column(db.Integer, db.ForeignKey('user.id'))

class LocksOwned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lockname = db.Column(db.String(64), index=True)
    ownedBy = db.Column(db.String(64), index=True)

class ResTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(100), index=True, primary_key=True)
    basedIn = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<Entered Company: {}, URL: {}, based in: {}>'.format(
            self.company, self.url, self.basedIn)