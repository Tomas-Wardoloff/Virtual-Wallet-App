from flask import Flask, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from config import config
from models.entities.User import User
from models.ModelUser import ModelUser

# Create flask application
app = Flask(__name__)

# Initialize flask-login
login_manager_app = LoginManager(app)

# Initialize flask-MySQLDB
database = MySQL(app)

# Initialize flask-WTF csrf
csrf = CSRFProtect(app)


# Load user through flask-login
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_by_id(database, id)


# Routes and views
@app.route("/")
def index():
    return redirect(url_for("signup"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        logged_user = ModelUser.login(
            database, request.form["email"], request.form["password"]
        )
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("home"))
            else:
                print("Invalid password...")
                return render_template("auth/login.html")
        else:
            print("User not found...")
            return render_template("auth/login.html")
    return render_template("auth/login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        if not ModelUser.check_user_existence(database, request.form["email"]):
            params = (
                request.form["first_name"].capitalize(),
                request.form["last_name"].capitalize(),
                request.form["email"],
                User.hash_password(request.form["password"]),
            )
            ModelUser.signup_user(database, params)
            login_user(
                ModelUser.login(
                    database, request.form["email"], request.form["password"]
                )
            )
            return redirect(url_for("home"))
        else:
            print("User already exists")
    return render_template("auth/register.html")


@app.route("/home")
@login_required
def home():
    return render_template("home.html")

# Error handlers
@app.errorhandler(401)
def status_401(error):
    return redirect(url_for("login"))

@app.errorhandler(404)
def status_404(error):
    return "<h1>Opps the requested URL was not found on this server</h1>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])
    csrf.init_app(app)
    app.run()
