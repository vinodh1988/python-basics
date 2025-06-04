def processPeople(**person): # receives keyword arguments as a dictionary
    data = {}
    for key, value in person.items():
        data[key] = value
    return data

def processPeople2(**person):
    return person
print("Person 1:", processPeople(sno=1, name="Alice", city="New York", country="USA"))  # Example call with all parameters
print("Person 2:", processPeople(sno=2, name="Bob", city="Chennai")) 
print("person 3:", processPeople2(sno =3, name="Roger")) # Example call with default country