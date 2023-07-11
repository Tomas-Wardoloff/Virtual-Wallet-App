from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from config import config

app = Flask(__name__)
app.config.from_object(config["development"])

database = MySQL(app)

login_manager_app = LoginManager(app)

csrf = CSRFProtect(app)
csrf.init_app(app)


@app.route("/")
def index():
    return redirect("/auth/login")


@app.errorhandler(401)
def status_401(error):
    return redirect(url_for("auth_bp.login"))


@app.errorhandler(404)
def status_404(error):
    return "<h1>Opps the requested URL was not found on this server</h1>", 404
