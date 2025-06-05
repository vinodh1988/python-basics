from connection import conn

cursor = conn.cursor()
sql = "INSERT INTO person (name, city) VALUES (%s, %s)"
values = ("John Doe", "New York")
cursor.execute(sql, values)
conn.commit()