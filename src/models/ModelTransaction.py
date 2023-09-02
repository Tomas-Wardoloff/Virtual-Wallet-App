from flask import jsonify
from .database import run_query, get_data


class ModelTransaction:
    @classmethod
    def upload_transaction(cls, params: tuple) -> None:
        upload_transaction_query = """
            INSERT INTO transactions (amount, date, type, category_name, description, user_id) VALUES (%s, %s, %s, %s, %s, %s)
        """
        run_query(upload_transaction_query, params)
        
    @classmethod
    def get_last_transactions_json(cls, user_id: int):
        get_transactions_query = """
            SELECT amount, date, type, category_name FROM transactions WHERE user_id = %s ORDER BY date DESC LIMIT 5
        """
        last_transactions_data = get_data(get_transactions_query, (user_id, ))
        
        transactions_list = []
        for row in last_transactions_data:
            transaction = {
                "Amount": row[0],
                "Date": row[1].strftime("%Y-%m-%d"),
                "Type": row[2],
                "Category": row[3]
            }
            transactions_list.append(transaction)        
        return jsonify({"transactions": transactions_list, "message": "last 5 transactions made"})
        
