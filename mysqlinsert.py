from connection import conn

def insert_persons(records):
    sql = "INSERT INTO person (name, city) VALUES (%s, %s)"
    cur = conn.cursor()
    cur.executemany(sql, records)
    conn.commit()
    print(f"{cur.rowcount} records inserted.")
    cur.close()

if __name__ == "__main__":
    records = []
    while True:
        name = input("Enter name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        city = input("Enter city: ")
        records.append((name, city))
    if records:
        insert_persons(records)
    else:
        print("No records to insert.")