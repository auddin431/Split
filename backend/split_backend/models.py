"""
Defines the database of the application
"""

from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False, unique=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False, unique=False)

    need_to_pay = db.Column(db.Integer, index=False, nullable=True, unique=False)
    owed = db.Column(db.Integer, index=False, nullable=True, unique=False)

    group_id = db.Column(db.Integer, ForeignKey("groups.id"), nullable=True, index=True)
    group = relationship("Group", backref="users", foreign_keys=[group_id])

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Purchase(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False, unique=False) #Grocery list for May
    total = db.Column(db.Integer, index=False, nullable=True, unique=True)

    group_id = db.Column(db.Integer, ForeignKey("groups.id"), nullable=False, index=True)
    group = relationship("Group", backref="purchases", foreign_keys=[group_id])

class Item(db.Model):
    """
    Represents an item which belongs to one purchase.
    It has a name and a count reuqest for each user.
    User has multiple items with different counts.
    """
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False, unique=False)
    count = db.Column(db.Integer, index=False, nullable=True, unique=False)

    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False, index=True)
    user = relationship("User", backref="items", foreign_keys=[user_id])



