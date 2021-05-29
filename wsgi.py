"""
Python script to run to start the API
"""

from split_backend import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
