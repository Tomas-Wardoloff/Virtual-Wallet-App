from MySQLdb import ProgrammingError, OperationalError 
def get_data(database, query: str) -> list:
    try:
        cursor = database.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except ProgrammingError as ex:
        raise ("Error de sintaxis en la consulta SQL: {}".format(ex))
    except OperationalError as ex:
        raise Exception("Error de conexión a la base de datos: {}".format(ex))
    except Exception as ex:
        raise Exception("Error inesperado: {}".format(ex))
    finally:
        database.connection.close()
