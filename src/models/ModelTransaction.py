from flask import jsonify
from .database import run_query, get_data
from datetime import date

class ModelTransaction: 
    @classmethod
    def upload_transaction(cls, params: tuple) -> None: 
        upload_transaction_query = """
            INSERT INTO transactions (amount, date, type, category_name, description, user_id) VALUES (%s, %s, %s, %s, %s, %s)
        """
        run_query(upload_transaction_query, params)
        
    @classmethod
    def get_transactions_data_as_json(cls, user_id: int, filter: str):
        current_date = date.today()
        if filter == "day" or filter == "month":
            if filter == "day": # [x] get the transactions by the current day
                filter = current_date
                get_transactions_query = """
                    SELECT amount, date, type, category_name FROM transactions WHERE user_id = %s and date = %s ORDER BY date DESC
                """
            elif filter == "month": # [x] get transactions by month 
                filter = current_date.month
                get_transactions_query = """
                    SELECT amount, date, type, category_name FROM transactions WHERE user_id = %s and EXTRACT(MONTH FROM date) = %s ORDER BY date DESC
                """
            last_transactions_data = get_data(get_transactions_query, (user_id, filter))
        elif filter == "summary": # [x] get all the transactions
            get_transactions_query = """
                SELECT amount, date, type, category_name FROM transactions WHERE user_id = %s ORDER BY date DESC
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
                  
        return jsonify({"transactions": transactions_list, "message": f"last transactions made by {filter}"}) 
