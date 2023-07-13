from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint(
    "main_bp", __name__, url_prefix="/home", template_folder="../../templates/"
)


@main_bp.route("/")
@login_required
def index():
    return render_template("home.html", title="Dashboard")

#@main_bp.route("/transaction/new")
#@login_required
#def index():
#    return render_template("home.html", title="New Transaction")