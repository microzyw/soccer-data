from flask import Blueprint, render_template, request, jsonify, session
from lib.utils import UtilsFunction

login = Blueprint('login', __name__)

@login.route('/', methods=['GET'])
def login_index():
    return render_template('login.html')

@login.route('/submitlogin', methods=['POST'])
def login_submitlogin():
    username = request.form.get('username')
    password = request.form.get('password')
    if username != "winner" or password != "666666":
        return jsonify({'success':'false'})
    else:
        token = UtilsFunction.getMD5(username + password)
        session['token'] = token
        return jsonify({'success':'true', 'token':token})