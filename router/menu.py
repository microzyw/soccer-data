from flask import Blueprint, render_template
from model.basic import login_required

menu = Blueprint('menu', __name__)

@menu.route('/', methods=['GET'])
@login_required
def menu_index():
    return render_template('menu.html')