# Load flask
from flask import Flask

# Create a function for our app
def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'fsdfasdfasdfadscv' # secures cookies and session info tfor this app

    return app

    