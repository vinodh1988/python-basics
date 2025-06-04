def sayHi():
    print("Hello, World! Hi there!") #function definition

sayHi() #function call

def sayHiTo(name):
    print(f"Hello, {name}! Hi there!") #function definition with parameter

sayHiTo("Alice") #function call with argument

def addNumbers(a, b):
    """Returns the sum of two numbers."""
    return a + b  # function definition with return value

print("addNumbers(5,10)", addNumbers(5, 10))  # function call with arguments