from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder = 'site_templates')

"""

Note that in the above code, 
some arguments are specified when creating a Blueprint object.
The first argument, "site" is the Blueprint name as a string,
which is used by flask's routing mechanism.
The second argument __name__ is the Blueprint's import name,
which Flask uses to locate the Blueprint's resources.
The third is telling Flask where to find the html to render. 

"""

@site.route('/')
#this just goes to our Homepage

def home():
    return render_template('index.html')


@site.route('/profile')
#if we need to loop through a database..
#think structurally what I need to do for final project here 

def profile():
    return render_template('profile.html')

#set whats in @site.route() to be same as def based on what I need for final project organization
