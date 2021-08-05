from os import environ

class Config:
    DB_URI = environ.get("DWS_MYSQL_DATABASE_URI", "localhost")
    DB_USER = environ.get("DWS_MYSQL_DATABASE_URI", "root")
    DB_PASSWORD = environ.get("DWS_MYSQL_DATABASE_URI", "")
    TEST_COMMAND = int(environ.get("DWS_TESTER_COMMAND", "1"))
    TEST_THRESHOLD = int(environ.get("DWS_TESTER_THRESHOLD", "3"))
    TEST_INTERVAL = int(environ.get("DWS_TESTER_INTERVAL", "5"))

