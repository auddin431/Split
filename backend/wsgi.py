"""
Python script to run to start the API
"""

from split_backend import create_app
from flask_cors import CORS

app = create_app()
CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
