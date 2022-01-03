from flask import Blueprint, render_template

# singin blueprint definition
singin = Blueprint('singin', __name__, static_folder='static', static_url_path='/singin', template_folder='templates')


# Routes
@singin.route('/singin')
def index():
    return render_template('singin.html')
