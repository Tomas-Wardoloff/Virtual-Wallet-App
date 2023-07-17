from .database import get_data, run_query
from .entities.User import User
from .entities.Wallet import Wallet


class ModelUser:
    @classmethod
    def login(cls, email, password) -> User | None:
        query = """
            SELECT id, first_name, last_name, email, password FROM users WHERE Email = %s
        """
        match_user = get_data(query, (email,))
        if match_user:
            return User(
                match_user[0][0],
                match_user[0][1],
                match_user[0][2],
                match_user[0][3],
                User.check_password(match_user[0][4], password),
            )
        return None

    @classmethod
    def get_user_by_id(cls, id) -> User | None:
        query = """
            SELECT id, first_name, last_name, email FROM users WHERE id = %s
        """
        match_user = get_data(query, (id,))
        if match_user:
            return User(*match_user[0], None)
        return None

    @classmethod
    def check_user_existence(cls, email) -> bool:
        query = """
            SELECT * FROM users WHERE Email = %s
        """
        match_user = get_data(query, (email,))
        return bool(match_user)

    @classmethod
    def signup_user(cls, params) -> None:
        create_user_query = """
            INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)
        """
        run_query(create_user_query, params)

    @classmethod
    def create_user_wallet(cls, params) -> bool:
        create_wallet_query = """
            INSERT INTO wallets (balance, currency, user_id) VALUES (%s, %s, %s)
        """
        run_query(create_wallet_query, params)

    @classmethod
    def get_user_wallet(cls, user_id) -> Wallet:
        get_wallet_query = """
            SELECT user_id, balance, currency FROM wallets WHERE user_id = %s
        """
        wallet_data = get_data(get_wallet_query, (user_id,))
        return Wallet(*wallet_data[0])
