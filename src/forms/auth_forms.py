from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,ValidationError)

from models.ModelUser import ModelUser


class RegistrationForm(FlaskForm):
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=20)]
    )
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(),],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_email(cls, email):
        if ModelUser.check_user_existence(email.data):
            raise ValidationError(
                f"That email is already taken. Please choose a different one")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(),],
    )
    submit = SubmitField("Sign In")

    def validate_email(cls, email):
        if not ModelUser.check_user_existence(email.data):
            raise ValidationError(f"User {email.data} was not found.")
