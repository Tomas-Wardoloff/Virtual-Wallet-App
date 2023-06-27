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
            user = User(
                match_user[0][0],
                match_user[0][1],
                User.check_password(match_user[0][2], user.Password),
            )
            return user
        return None
