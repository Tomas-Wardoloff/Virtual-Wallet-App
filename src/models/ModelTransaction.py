from .database import run_query


class ModelTransaction:
    @classmethod
    def upload_transaction(cls, params) -> None:
        upload_transaction_query = """
            INSERT INTO transactions (amount, date, type, category_name, description, user_id) VALUES (%s, %s, %s, %s, %s, %s)
        """
        run_query(upload_transaction_query, params)
