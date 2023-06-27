from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_mysqldb import MySQL

from config import config
from models.entities.User import User
from models.ModelUser import ModelUser

app = Flask(__name__)

login_manager_app = LoginManager(app)

database = MySQL(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_by_id(database, id)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(None, request.form["email"], request.form["password"])
        logged_user = ModelUser.login(database, user)
        if logged_user != None:
            if logged_user.Password:
                login_user(logged_user)
                return redirect(url_for("home"))
    return render_template("auth/login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/signup")
def signup():
    return render_template("auth/register.html")


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
