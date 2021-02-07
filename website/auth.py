from flask import Blueprint

# we will define that this file is the blueprint of our applciaiton; meaning it has a bunch of roots inside of it
auth = Blueprint('auth',  __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"