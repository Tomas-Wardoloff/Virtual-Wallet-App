from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from forms.transaction_forms import TransactionForm
from models.ModelCategories import ModelCategory
from models.ModelTransaction import ModelTransaction
from models.ModelUser import ModelUser
from models.ModelWallet import ModelWallet

main_bp = Blueprint(
    "main_bp", __name__, url_prefix="/home", template_folder="../../templates/"
)


@main_bp.route("/", methods=["GET"])
@login_required
def index():
    user_wallet = ModelUser.get_user_wallet(current_user.id)
    return render_template(
        "home.html",
        title="Dashboard",
        wallet=user_wallet,
    )


@main_bp.route("/new_transaction", methods=["GET", "POST"])
@login_required
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction_params = (
            form.amount.data,
            form.date.data,
            form.type.data,
            form.description.data,
            form.category.data,
            current_user.id,
        )
        print(transaction_params)
        ModelTransaction.upload_transaction(transaction_params)

        user_wallet = ModelUser.get_user_wallet(current_user.id)
        ModelWallet.update_balance(user_wallet, form.amount.data, form.type.data)
        flash(f"transaction uploaded successfully!", "success")
        return redirect(url_for("main_bp.index"))
    return render_template("new_transaction.html", title="New Transaction", form=form)


@main_bp.route("/transactions/<int:user_id>/<filter_option>", methods=["GET"])
def get_transaction(user_id, filter_option):
    try:
        data = ModelTransaction.get_transactions_data(user_id, filter_option)
        return data
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main_bp.route("/categories/<int:user_id>/<filter_option>", methods=["GET"])
def get_categories(user_id, filter_option):
    try:
        data = ModelCategory.get_categories_totals(user_id, filter_option)
        return data
    except Exception as e:
        return jsonify({"error": str(e)}), 500
