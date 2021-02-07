from flask import Blueprint

# we will define that this file is the blueprint of our applciaiton; meaning it has a bunch of roots inside of it
views = Blueprint('auth',  __name__)

# decorator: define a route: to define a view we use @blueprintname.route('path'); below '/' indicates home page
# when ever we hit the route, we call the function
@views.route('/')  
def home():
    return "<h1>test</h1>"