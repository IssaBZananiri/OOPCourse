'''
Exercise 4 - Create a Shape, and Calculate the Parameters and Areas
Author: Issa B. Zananiri
Date: 23/11/2023
Learning Classes and Objects
'''
import math
# This class is the Shape Class
class Shape: 
    def _calculate_area(self):
        pass

    def _calculate_perimeter(self):
        pass

# Subclass for a circle
class Circle(Shape):
    # Initialize if it is a circle, you need a radius
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    # Override the Method in the parent class.
    def _calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    # Override the Method in the parent class.
    def _calculate_perimeter(self):
        return (math.pi * (self.radius) * 2)


class Rectangle(Shape):
    
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
    
    # Override the Method in the parent class.
    def _calculate_area(self):
        return (self.length * self.width)
    
    # Override the Method in the parent class.
    def _calculate_perimeter(self):
        return (2*self.length + 2*self.width)

# This is interesting, you call the super class, and then you give both parameters the same parameter
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


class Triangle(Shape):
    def __init__(self, length, height):
        super().__init__()
        self.side_length = length
        self.height = height
    
    # Override the Method in the parent class.
    def _calculate_area(self):
        return (0.5 * self.side_length * self.height)


square1 = Square(10)
print(square1._calculate_area())
print(square1._calculate_perimeter())

print(Triangle(10,10)._calculate_area())
triangle1 = Triangle(10,10)
print(triangle1._calculate_area())


        