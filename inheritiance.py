class Shape():
    def __init__(self, name):
        self.name = name
        

    def show(self):
        print(f"This is a {self.name}.")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")  # Call the parent class constructor
        self.length = length
        self.width = width

    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    

    def area(self):
        return self.length * self.width

    def show(self):
        super().show()  # Call the parent class show method
        print(f"Length: {self.length}, Width: {self.width}, Area: {self.area()}")

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")  # Call the parent class constructor
        self.side = side

    def __repr__(self):
        return f"Square(side={self.side})"
    
    def area(self):
        return self.side * self.side
    
    def show(self):
        super().show()  # Call the parent class show method
        print(f"Side: {self.side}, Area: {self.area()}")


squar1= Square(5)
squar2= Square(10)
rect1= Rectangle(5, 10)
rect2= Rectangle(10, 20)
squar1.show()
squar2.show()
rect1.show()
rect2.show()