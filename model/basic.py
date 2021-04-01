from functools import wraps
from flask import request, url_for, redirect, session, escape
from lib.utils import UtilsFunction

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = session.get('token')
        temp = "winner" + "666666"
        if token == UtilsFunction.getMD5(temp):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login.login_index"))
    return wrapper