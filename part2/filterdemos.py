numbers= [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

tendivisibles = lambda x: x % 10 == 0

print(list(filter(tendivisibles, numbers)))

numbers = [34,536,345,34,6666,343,434,123,356,12,53,565,325,252]
print(list(filter(lambda x: 100 <= x <= 999, numbers)))

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank",
         "Grace", "Hannah", "Ian", "Jack", "Kathy", "Liam", "Mia", "Nina", "Oscar", "Paul"]

print(list(filter(lambda name: len(name)==3 , names)))

