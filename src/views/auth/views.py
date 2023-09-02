from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import login_manager_app
from forms.auth_forms import LoginForm, RegistrationForm
from models.entities.User import User
from models.ModelUser import ModelUser

auth_bp = Blueprint(
    "auth_bp", __name__, url_prefix="/auth", template_folder="../../templates/auth/"
)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_by_id(id)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.index"))

    form = LoginForm()
    if form.validate_on_submit():
        logged_user = ModelUser.login(form.email.data, form.password.data)

        if logged_user.password:
            login_user(logged_user)
            flash(f"You have been logged in as {form.email.data}!", "success")
            return redirect(url_for("main_bp.index"))
        else:
            flash(f"Login Unseccessful. Please check email and password", "danger")
            return render_template("login.html", form=form, title="Login")

    return render_template("login.html", form=form, title="Login")


@auth_bp.route("signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        if not ModelUser.check_user_existence(form.email.data):
            user_params = (
                form.first_name.data.capitalize(),
                form.last_name.data.capitalize(),
                form.email.data,
                User.hash_password(form.password.data),
            )
            ModelUser.signup_user(user_params)

            user_created = ModelUser.login(form.email.data, form.password.data)
            ModelUser.create_user_wallet((float(0), "USD", user_created.id))

            login_user(user_created)
            flash(f"Account created for {form.email.data}!", "success")
            return redirect(url_for("main_bp.index"))
    return render_template("register.html", form=form, title="Register")
