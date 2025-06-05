from connection import conn

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
