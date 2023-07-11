from app import database, login_manager_app
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required, login_user, logout_user

from models.entities.User import User
from models.ModelUser import ModelUser

auth_bp = Blueprint(
    "auth_bp", __name__, url_prefix="/auth", template_folder="../../templates/auth/"
)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_by_id(database, id)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        logged_user = ModelUser.login(
            database, request.form["email"], request.form["password"]
        )
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("main_bp.index"))
            else:
                flash("Invalid password...")
                return render_template("login.html")
        else:
            flash("User not found...")
            return render_template("login.html")
    return render_template("login.html")


@auth_bp.route("signup", methods=["GET", "POST"])
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
            flash("User successfully registered!")
            return redirect("/home")
        else:
            flash("User already exists")
    return render_template("register.html")
