"""
Handles routes for user registration and authentication
"""

from .models import db, User
from flask import Blueprint, session, g, request

auth_bp = Blueprint(
    "auth_bp", __name__
)

@auth_bp.route('/split_api/user/create', methods=["GET"])
def api_reg_user():
    params = request.args
    username = params.get("name")
    passwd = params.get("passwd")
    #TODO: Create user

    return 1 #success


