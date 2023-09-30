from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DecimalField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, Optional


class TransactionForm(FlaskForm):
    categories_names = [
        (1, "Groceries"),
        (2, "Utilities"),
        (3, "Transportation"),
        (4, "Housing"),
        (5, "Eating Out"),
        (6, "Entertainment"),
        (7, "Clothing"),
        (8, "Healthcare"),
        (9, "Education"),
        (10, "Miscellaneous"),
    ]

    amount = DecimalField("Amount", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    type = SelectField(
        "Type", validators=[DataRequired()], choices=["Expense", "Income"]
    )
    description = TextAreaField("Description", validators=[Optional(), Length(max=256)])
    category = SelectField(
        "Category", validators=[DataRequired()], coerce=int, choices=categories_names
    )
    submit = SubmitField("Upload transaction")
