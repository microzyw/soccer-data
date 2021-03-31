from flask import Blueprint, render_template, request, jsonify, session

login = Blueprint('login', __name__)

@login.route('/', methods=['GET'])
def login_index():
    return render_template('login.html')