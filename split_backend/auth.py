"""
Handles routes for user registration and authentication
"""
import functools
from .models import db, User
from flask import Blueprint, session, g, request

auth_bp = Blueprint(
    "auth_bp", __name__
)

@auth_bp.route('/split_api/user/create', methods=["GET", "POST"])
def api_reg_user():
    """
    Register a user by providing a username and password
    :return: 999 if already exists, or the new user id is success
    """
    params = request.args
    username = params.get("username")
    passwd = params.get("password")

    existing_user = User.query.filter_by(name=username).first()

    if existing_user is not None:
        #error, username already in use
        return str(999)
    else:
        new_user = User(name=username, need_to_pay=0, owed=0)
        new_user.name = username
        new_user.group_id = 0
        new_user.set_password(passwd)
        db.session.add(new_user)
        db.session.commit()
        session.clear()
        session["user_id"] = new_user.id
        return str(new_user.id)

    return str(1) #success

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()

