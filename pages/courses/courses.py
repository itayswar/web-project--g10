from flask import Blueprint, render_template

# courses blueprint definition
courses = Blueprint('courses', __name__, static_folder='static', static_url_path='/courses', template_folder='templates')


# Routes
@courses.route('/courses')
def index():
    return render_template('courses.html')
