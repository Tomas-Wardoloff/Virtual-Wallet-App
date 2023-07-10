from MySQLdb import ProgrammingError, OperationalError


def get_data(database, query: str, params: tuple = ()) -> list:
    try:
        with database.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    except ProgrammingError as ex:
        raise SyntaxError(f"Error de sintaxis en la consulta SQL: {ex}")
    except OperationalError as ex:
        raise Exception(f"Error de conexión a la base de datos: {ex}")
    except Exception as ex:
        raise Exception(f"Error inesperado: {ex}")


def run_query(database, query: str, params: tuple = ()) -> None:
    try:
        with database.connection.cursor() as cursor:
            cursor.execute(query, params)
            database.connection.commit()
            return None
    except Exception as ex:
        raise Exception(f"Error inesperado: {ex}")
