from flask import Blueprint, redirect, render_template, request, url_for

main_bp = Blueprint(
    "main_bp", __name__, url_prefix="/home", template_folder="../../templates/"
)


@main_bp.route("/")
def index():
    return render_template("home.html")
