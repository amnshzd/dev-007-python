import mysql.connector
from mysql.connector import Error
from config import Config

try:
    conn = mysql.connector.connect(host=Config.DB_URI,
                         user=Config.DB_USER,
                         password=Config.DB_PASSWORD)
    if conn.is_connected():
       cursor = conn.cursor()
       print("1")

except Error as e :
    print("0")
    print("Error Reason : ", e)
