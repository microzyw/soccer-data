from flask import Flask, url_for, redirect, request
from router.login import login

app = Flask(__name__)
app.register_blueprint(login, url_prefix="/login")

@app.route('/', methods=['POST','GET'])
def index():
    return redirect(url_for("login.login_index"))

if __name__ == '__main__':
    app.run()