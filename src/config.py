import decouple


class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = decouple.config("SECRET_KEY")
    MYSQL_HOST = decouple.config("MYSQL_HOST")
    MYSQL_USER = decouple.config("MYSQL_USER")
    MYSQL_PASSWORD = decouple.config("MYSQL_PASSWORD")
    MYSQL_DB = decouple.config("MYSQL_DB")


config = {"development": DevelopmentConfig}
