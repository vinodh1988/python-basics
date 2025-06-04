def getAnything(x):
    print(f"You passed: {x} and its type is {type(x)}")	

def HelloWorld():
    print("Hello, World!")
getAnything(10)  # Integer
getAnything(3.14)  # Float
getAnything("Hello")  # String
getAnything([1, 2, 3])  # List
getAnything((1, 2))  # Tuple
getAnything({"key": "value"})  # Dictionary
getAnything({1, 2, 3})  # Set
getAnything(None)  # NoneType
getAnything(True)  # Boolean    
getAnything(HelloWorld)  # Function