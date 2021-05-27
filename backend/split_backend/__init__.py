"""
Creates the backend application
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .models import User

        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(routes.api)
        db.create_all()

        return app


