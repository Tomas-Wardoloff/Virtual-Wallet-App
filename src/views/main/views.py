from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from forms.transaction_forms import TransactionForm
from models.ModelTransaction import ModelTransaction
from models.ModelUser import ModelUser
from models.ModelWallet import ModelWallet


main_bp = Blueprint(
    "main_bp", __name__, url_prefix="/home", template_folder="../../templates/"
)


@main_bp.route("/")
@login_required
def index():
    user_wallet = ModelUser.get_user_wallet(current_user.id)
    return render_template("home.html", title="Dashboard", wallet=user_wallet)


@main_bp.route("/new_transaction", methods=["GET", "POST"])
@login_required
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction_params = (
            form.amount.data,
            form.date.data,
            form.type.data,
            form.category.data,
            form.description.data,
            current_user.id,
        )
        print(transaction_params)
        ModelTransaction.upload_transaction(transaction_params)

        user_wallet = ModelUser.get_user_wallet(current_user.id)
        ModelWallet.update_balance(user_wallet, form.amount.data, form.type.data)
        flash(f"transaction uploaded successfully!", "success")
        return redirect(url_for("main_bp.index"))
    return render_template("new_transaction.html", title="New Transaction", form=form)
