from datetime import date

from flask import jsonify

from .database import get_data


class ModelCategory:
    @classmethod
    def get_categories_totals(cls, user_id: int, filter_option: str):
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

        params = (user_id, filter_option) if filter_value is not None else (user_id,)

        all_categories = get_data(get_categories_query, params)

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
    def get_income_expense_totals(cls, user_id):
        pass