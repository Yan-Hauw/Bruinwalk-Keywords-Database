import mysql.connector
from mysql.connector import errorcode

# constants
from constants.server_keys import mysqlServer
from constants.scraping_keywords import scraping_keywords


def create_table(department):

    DB_NAME = "departments"

    w1, w2, w3, w4, w5, w6, w7 = scraping_keywords

    TABLES = {}
    TABLES[
        department
    ] = "CREATE TABLE {department} (course_name varchar(30) NOT NULL, lecturer varchar(30) NOT NULL, {w1} varchar(30) NOT NULL, {w2} varchar(30) NOT NULL, {w3} varchar(30) NOT NULL, {w4} varchar(30) NOT NULL, {w5} varchar(30) NOT NULL, {w6} varchar(30) NOT NULL, {w7} varchar(30) NOT NULL) ENGINE=InnoDB"

    template_table_values = {
        "department": department,
        "w1": w1,
        "w2": w2,
        "w3": w3,
        "w4": w4,
        "w5": w5,
        "w6": w6,
        "w7": w7,
    }

    cnx = mysql.connector.connect(
        user=mysqlServer.username,
        password=mysqlServer.password,
    )
    cursor = cnx.cursor()

    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
            )
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    # use database, create if not exists

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    # create tables as specified in TABLES dictionary

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end="")
            cursor.execute(table_description.format(**template_table_values))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()


create_table("CS")
