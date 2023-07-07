from .database import get_data, run_query
from .entities.User import User


class ModelUser:
    @classmethod
    def login(cls, database, email, password) -> User | None:
        query = """
            SELECT UserId, Email, First_name, Last_name, Password FROM users WHERE Email = %s
        """
        match_user = get_data(database, query, (email,))
        if match_user:    
            return User(
                match_user[0][0],
                match_user[0][1],
                User.check_password(match_user[0][2], password),
                match_user[0][2],
                match_user[0][3],
            )
        return None

    @classmethod
    def get_user_by_id(cls, database, id) -> User | None:
        query = """
            SELECT UserId, Email, First_name, Last_name FROM users WHERE UserId = %s
        """
        match_user = get_data(database, query, (id,))
        if match_user != ():
            return User(
                match_user[0][0],
                match_user[0][1],
                None,
                match_user[0][2],
                match_user[0][3],
            )
        return None

    @classmethod
    def check_user_existence(cls, database, email) -> bool:
        query = """
            SELECT * FROM users WHERE Email = %s
        """
        match_user = get_data(database, query, (email,))
        if match_user == ():
            return False
        return True

    @classmethod
    def signup_user(cls, database, params) -> None:
        create_user_query = """
            INSERT INTO users (First_name, Last_name, Email, Password) VALUES (%s, %s, %s, %s)
        """
        run_query(database, create_user_query, params)
        print("User successfully registered!")
