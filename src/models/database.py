def get_data(database, query: str) -> list:
    cursor = database.connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as ex:
        raise Exception(ex)
