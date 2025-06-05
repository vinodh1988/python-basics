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
cursor = conn.cursor()

# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS person (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    city VARCHAR(100)
)
"""
cursor.execute(create_table_query)

print("Table 'person' created successfully.")

cursor.close()
conn.close()
