person = {
    "sno": 1,
    "name": "John",
    "city": "New York",
    "weight": 70.5,
    "age": 30,	
}
# Accessing dictionary elements
print("Serial Number:", person["sno"])
print("Name:", person["name"])
print("City:", person["city"])
print("Weight:", person["weight"])
print("Age:", person["age"])

for key, value in person.items():
    print(f"{key}: {value}")

person["email"] = "john@gmail.com"

print("After adding email:")
print("Person details:", person)