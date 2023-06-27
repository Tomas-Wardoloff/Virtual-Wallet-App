from werkzeug.security import check_password_hash

class User:
    def __init__(self, id, email, password) -> None:
        self.UserId = id
        self.Email = email
        self.Password = password
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)