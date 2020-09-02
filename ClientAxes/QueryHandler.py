#Trevor O'Hearn
#9/2/20
#QueryHandler.py
#Handles all queries made by the front end

#installs
# pip install mysql-connector-python

#import passwords and such
import config

#database comms
import mysql.connector
from mysql.connector import errorcode

#Database name
db_name = 'Clients'

#create cursor for database
# cnx = getConnection()
# cursor = cnx.cursor()

def getConnection(config):
    cnx = mysql.connector.connect(
        host = config.credentials['host'],
        user = config.credentials['user'],
        passwd = config.credentials['passwd']
    )


#create Database
def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database)
        )
    except mysql.connector.Error as err:
        print('Failed to create database {} : {}'.format(database, err))
        exit(1)

def database_instatiation_check(cursor, db_name)
    # check to see if the database already
    try:
        cursor.execute("USE {}".format(db_name))

    #if the previous line fails because there isn't a db by that name run this line

    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, db_name)
            print("Database {} created successfully.".format(db_name))
            cnx.database = db_name
        else:
            print(err)
            exit(1)

def makeTables(cursor, TABLES):
    for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

#use cnx.commit() to finish any query made with execute
# or it will not reflect in database, only in current session

# ALWAYS CLOSE CURSOR AND CONNECTION OR RISK LOSING $$$
cursor.close()
cnx.close()

#example of single insert
# # insert statement to add an employee
# add_employee = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")
# # Insert new employee
# cursor.execute(add_employee, data_employee)
# # Make sure data is committed to the database
# cnx.commit()


#example of insert many
#create a list of records
#
# data = [
#   ('Jane', date(2005, 2, 12)),
#   ('Joe', date(2006, 5, 23)),
#   ('John', date(2010, 10, 3)),
# ]
#
# #create the insert statment
# stmt = "INSERT INTO employees (first_name, hire_date) VALUES (%s, %s)"
#
# #insert all of the records and commit it
# cursor.executemany(stmt, data)
# cnx.commit()


#example of query code
#
# query = ("SELECT first_name, last_name, hire_date FROM employees "
#          "WHERE hire_date BETWEEN %s AND %s")
#
# hire_start = datetime.date(2006, 1, 1)
# hire_end = datetime.date(2006, 12, 31)
#
# cursor.execute(query, (hire_start, hire_end))
#
#then use fetchone(), fetchmany(), fetchall()
#rows = cursor.fetchall()
# for row in rows:
#    print(row)
