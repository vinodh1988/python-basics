listx=[1,2,3,4,5,6,7,8,9,10]

def mul11(x):
    return x * 11

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

def uppercase_name(name):
    return name.upper()

print(list(map(mul11,listx)))
print(list(map(lambda x: x * 11, listx)))

print(list(map(uppercase_name, names)))
print(list(map(lambda name: name.upper(), names)))

print(list(map(lambda x: x * x, listx)))
print(list(map(lambda x: x**3, listx)))
