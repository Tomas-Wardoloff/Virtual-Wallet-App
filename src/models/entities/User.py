from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, email, password) -> None:
        self.id = id
        self.email = email
        self.password = password

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)
