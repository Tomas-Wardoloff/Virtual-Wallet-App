from flask import Blueprint, render_template
from flask_login import current_user, login_required

from models.ModelUser import ModelUser

main_bp = Blueprint(
    "main_bp", __name__, url_prefix="/home", template_folder="../../templates/"
)


@main_bp.route("/")
@login_required
def index():
    wallet = ModelUser.get_user_wallet(current_user.id)
    return render_template("home.html", title="Dashboard", wallet=wallet)
