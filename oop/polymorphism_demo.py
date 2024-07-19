# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

# Test the classes
if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Circle(5)
    ]

    for shape in shapes:
        print(f"The area of the shape is: {shape.area()}")
