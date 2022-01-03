from flask import Blueprint, render_template, redirect, url_for
from utilities.db.USERS import USERS
from utilities.db.CONTACTS import CONTACTS
from utilities.db.VIDEOS import VIDEOS



# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    return render_template('homepage.html',)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
