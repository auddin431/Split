"""
Creates the backend application
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#from flask_admin import Admin

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .models import User

        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(routes.api_bp)
        db.create_all()

        #admin = Admin(app, name='microblog', template_mode='bootstrap3')

        return app


