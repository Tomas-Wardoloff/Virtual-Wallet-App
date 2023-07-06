from .database import get_data
from .entities.User import User


class ModelUser:
    @classmethod
    def login(cls, database, user):
        query = """
            SELECT UserId, Email, Password, First_name, Last_name FROM users WHERE Email = %s
        """
        match_user = get_data(database, query, (user.email,))
        if match_user != ():
            return User(
                match_user[0][0],
                match_user[0][1],
                User.check_password(match_user[0][2], user.password),
                match_user[0][3],
                match_user[0][4],
            )
        return None

    @classmethod
    def get_user_by_id(cls, database, id):
        query = """
            SELECT UserId, Email FROM users WHERE UserId = %s
        """
        match_user = get_data(database, query, (id,))
        if match_user != ():
            return User(match_user[0][0], match_user[0][1], None, None, None)
        return None
