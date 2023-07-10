from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin):
    def __init__(self, id, first_name, last_name, email, password) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @staticmethod 
    def check_password(hashed_password: str, password: str) -> bool:
        return check_password_hash(hashed_password, password)

    @staticmethod 
    def hash_password(password: str) -> str:
        return generate_password_hash(password)
