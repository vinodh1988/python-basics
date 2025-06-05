import os
import mysql.connector

# Get credentials from environment variables
host = os.environ.get('MYSQLHOST')
user = os.environ.get('MYSQLUSER')
password = os.environ.get('MYSQLPASS')

# Connect to MySQL and specify the database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='python'
)