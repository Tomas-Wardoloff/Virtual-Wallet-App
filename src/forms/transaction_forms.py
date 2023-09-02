from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    DateField,
    DecimalField,
    SelectField,
    TextAreaField,
    StringField,
)
from wtforms.validators import DataRequired, Length, Optional


class TransactionForm(FlaskForm):
    categories_names = [
        "Groceries",
        "Utilities",
        "Transportation",
        "Housing",
        "Eating Out",
        "Entertainment",
        "Clothing",
        "Healthcare",
        "Education",
        "Miscellaneous",
    ]

    amount = DecimalField("Amount", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    type = SelectField(
        "Type", validators=[DataRequired()], choices=["Expense", "Income"]
    )
    description = TextAreaField("Description", validators=[Optional(), Length(max=256)])
    category = SelectField(
        "Category", validators=[DataRequired()], choices=categories_names
    )
    submit = SubmitField("Upload transaction")
