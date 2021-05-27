"""
Defines the database of the application
"""

from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), index=True, nullable=False, unique=False)
    last_name = db.Column(db.String(100), index=True, nullable=False, unique=False)

    need_to_pay = db.Column(db.Integer, index=False, nullable=True, unique=False)
    owed = db.Column(db.Integer, index=False, nullable=True, unique=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.first_name)



