import os
import pymysql

# Get username from Cloud 9 Workspace
# (Modify this variable if running on a different environment)
username = os.getenv('C9_User')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             # user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
