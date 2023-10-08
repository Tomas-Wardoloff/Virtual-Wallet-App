from datetime import date

from flask import jsonify

from .database import get_data, run_query


class ModelTransaction:
    @classmethod
    def upload_transaction(cls, params: tuple) -> None:
        upload_transaction_query = """
            INSERT INTO transactions (amount, date, type, description, category_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)
        """
        run_query(upload_transaction_query, params)

    @classmethod
    def get_transactions_data(cls, user_id: int, filter_option: str):
        current_date = date.today()
        get_transactions_query = None

        if filter_option == "day":
            get_transactions_query = """
                SELECT t.amount, t.date, t.type, c.name
                FROM transactions AS t
                INNER JOIN categories AS c ON t.category_id = c.id
                WHERE t.user_id = %s and t.date = %s 
                ORDER BY t.date DESC
            """
            filter_value = current_date

        elif filter_option == "month":
            get_transactions_query = """
                SELECT t.amount, t.date, t.type, c.name
                FROM transactions AS t
                INNER JOIN categories AS c ON t.category_id = c.id
                WHERE t.user_id = %s and EXTRACT(MONTH FROM t.date) = %s 
                ORDER BY t.date DESC
            """
            filter_value = current_date.month

        elif filter_option == "summary":
            get_transactions_query = """
                SELECT t.amount, t.date, t.type, c.name 
                FROM transactions 
                INNER JOIN categories AS c ON t.category_id = c.id
                WHERE t.user_id = %s 
                ORDER BY t.date DESC
            """
            filter_value = None

        last_transactions_data = get_data(
            get_transactions_query, (user_id, filter_value)
        )

        transactions_list = []  # format the data in a list
        for row in last_transactions_data:
            transaction = {
                "Amount": row[0],
                "Date": row[1].strftime("%Y-%m-%d"),
                "Type": row[2],
                "Category": row[3],
            }
            transactions_list.append(transaction)

        return jsonify(  # return a json
            {
                "transactions": transactions_list,
                "message": f"last transactions made by {filter_value}",
            }
        )
