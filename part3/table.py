people = [
     {"sno": 1, "name": "Alice",   "city": "New York"},
     {"sno": 2, "name": "Bob",     "city": "Los Angeles"},
     {"sno": 3, "name": "Charlie", "city": "Chicago"},
     {"sno": 4, "name": "David",   "city": "Houston"},
     {"sno": 5, "name": "Eve",     "city": "Phoenix"},
     {"sno": 6, "name": "Frank",   "city": "Philadelphia"},
     {"sno": 7, "name": "Grace",   "city": "San Antonio"},
     {"sno": 8, "name": "Helen",   "city": "San Diego"},
     {"sno": 9, "name": "Ivy",     "city": "Dallas"},
     {"sno": 10, "name": "Jack",  "city": "San Jose"}
]

with open("people.txt", "w") as f:
    f.write(f"{'SNo':<5}{'Name':<15}{'City'}\n")
    f.write("-" * 30 + "\n")
    for person in people:
        f.write(f"{person['sno']:<5}{person['name']:<15}{person['city']}\n")
