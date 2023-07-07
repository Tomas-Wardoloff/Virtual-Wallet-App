from MySQLdb import ProgrammingError, OperationalError


def get_data(database, query: str, params: tuple = ()) -> list:
    try:
        cursor = database.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except ProgrammingError as ex:
        raise ("Error de sintaxis en la consulta SQL: {}".format(ex))
    except OperationalError as ex:
        raise Exception("Error de conexión a la base de datos: {}".format(ex))
    except Exception as ex:
        raise Exception("Error inesperado: {}".format(ex))


def run_query(database, query: str, params: tuple = ()) -> None:
    try:
        cursor = database.connection.cursor()
        cursor.execute(query, params)
        database.connection.commit()
        return None
    except Exception as ex:
        raise Exception("Error inesperado: {}".format(ex))
