from .database import get_data
from .entities.User import User


class ModelUser:
    @classmethod
    def login(cls, database, user):
        query = """
            SELECT UserId, Email, Password FROM users WHERE Email = '{}'
        """.format(user.Email)
        match_user = get_data(database, query)
        if match_user != []:
            return User(
                match_user[0][0],
                match_user[0][1],
                User.check_password(match_user[0][2], user.Password),
            )
        return None

    @classmethod
    def get_user_by_id(cls, database, id):
        query = """
            SELECT UserId, Email FROM users WHERE UserId = '{}'
        """.format(id)
        match_user = get_data(database, query)
        if match_user != []:
            return User(match_user[0][0], match_user[0][1], None)
        return None