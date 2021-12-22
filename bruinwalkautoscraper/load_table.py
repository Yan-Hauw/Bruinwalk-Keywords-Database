import mysql.connector
from mysql.connector import errorcode

# constants
from constants.server_keys import mysqlServer

cnx = mysql.connector.connect(
    user=mysqlServer.username, password=mysqlServer.password, database="departments"
)
cursor = cnx.cursor()

cursor.execute()


cursor.close()
cnx.close()
