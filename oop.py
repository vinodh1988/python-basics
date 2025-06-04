# wrapping/grouping data and methods together
# Encapsulation 
# We want to represent an entity with its properties and behaviors
# so that we can model real-world objects in our code.

class Person:
    def __init__(self, sno,name, age):
        self.sno = sno  # public attribute
        self.name = name  # public attribute
        self.age = age    # public attribute

    def show(self):
        """Display person's details."""
        print(f"Person  sno: {self.sno} Name,: {self.name}, Age: {self.age}")

person1= Person(1, "Alice", 30) # will call __init__ method
person2 = Person(2, "Bob", 25)
person3 = Person(3, "Charlie", 35)

person1.show()
person2.show()
person3.show()