from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET', 'POST']) #always going to be a list and always be methods, you know what they say, be methods
def signup(): 
    return render_template('signup.html')

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')