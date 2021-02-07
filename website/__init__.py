# Load flask
from flask import Flask

# Create a function for our app
def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'fsdfasdfasdfadscv' # secures cookies and session info tfor this app

    # import blueprint
    from .views import views
    from .auth import auth

    # register blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app

    