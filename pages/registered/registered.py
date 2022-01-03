from flask import Blueprint, render_template

# registered blueprint definition
registered = Blueprint('registered', __name__, static_folder='static', static_url_path='/registered', template_folder='templates')


# Routes
@registered.route('/registered')
def index():
    return render_template('courses.html')
