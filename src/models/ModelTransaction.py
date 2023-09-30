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
    def get_categories_totals(
        cls, user_id: int, filter_option: str
    ):  # [ ] puedo cambiar la estructura de la base de datos para poder directamente el id de la categoria a la que hago referencia y no una columna de category_name
        current_date = date.today()
        get_categories_query = None

        if filter_option == "day":
            get_categories_query = """
                SELECT c.name, SUM(t.amount) 
                FROM transactions AS t
                INNER JOIN categories AS c ON t.category_id = c.id
                WHERE t.user_id = %s and t.date = %s
                GROUP BY c.name
            """
            filter_value = current_date

        elif filter_option == "month":
            get_categories_query = """
                SELECT c.name, SUM(t.amount) 
                FROM transactions AS t
                INNER JOIN categories AS c ON t.category_id = c.id 
                WHERE t.user_id = %s and EXTRACT(MONTH FROM t.date) = %s
                GROUP BY c.name
            """
            filter_value = current_date.month

        elif filter_option == "summary":
            get_categories_query = """
                    SELECT c.name, SUM(t.amount) 
                    FROM transactions AS t
                    INNER JOIN categories AS c ON t.category_id = c.id
                    WHERE t.user_id = %s
                    GROUP BY c.name
                """
            filter_value = None

        all_categories = get_data(get_categories_query, (user_id, filter_value))

        categories_dict = {}
        for category_data in all_categories:
            category_name, total_amount = category_data[0], category_data[1]
            categories_dict[category_name] = total_amount

        return jsonify(
            {
                "categories": categories_dict,
                "message": "categories names and their amounts",
            }
        )

    @classmethod
    def get_transactions_data(cls, user_id: int, filter_option: str):
        current_date = date.today()
        get_transactions_query = None

        if filter_option == "day":  # [x] get the transactions by the current day
            get_transactions_query = """
                SELECT t.amount, t.date, t.type, c.name
                FROM transactions AS t
                INNER JOIN categories AS c ON t.category_id = c.id
                WHERE t.user_id = %s and t.date = %s 
                ORDER BY t.date DESC
            """
            filter_value = current_date

        elif filter_option == "month":  # [x] get transactions by month
            get_transactions_query = """
                SELECT t.amount, t.date, t.type, c.name
                FROM transactions AS t
                INNER JOIN categories AS c ON t.category_id = c.id
                WHERE t.user_id = %s and EXTRACT(MONTH FROM t.date) = %s 
                ORDER BY t.date DESC
            """
            filter_value = current_date.month

        elif filter_option == "summary":  # [x] get all the transactions
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
