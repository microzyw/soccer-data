from flask import Flask, url_for, redirect, request
from router.login import login
from router.menu import menu
from router.odds import odds

app = Flask(__name__)
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(menu, url_prefix="/menu")
app.register_blueprint(odds, url_prefix="/odds")

app.config["SECRET_KEY"] = "soccer-data-scan"

@app.route('/', methods=['POST','GET'])
def index():
    return redirect(url_for("login.login_index"))

if __name__ == '__main__':
    app.run()