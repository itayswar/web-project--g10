from flask import Blueprint, render_template

# QA blueprint definition
QA = Blueprint('QA', __name__, static_folder='static', static_url_path='/QA', template_folder='templates')


# Routes
@QA.route('/QA')
def index():
    return render_template('QA.html')
