'''
Program 1: Circle Class, with calculation of Area and Parameter
Author: Issa B. Zananiri 22/11/2023
Exercise is DONE!
'''
import math as _m


class Circle:
# Circle class that calculates the area and circumference
# Gets Radius
#     
    def __init__(self, radius):
        self.radius = radius
    
    # Calculate the circumference of the circle
    def circumference(self):
        return (2 * self.radius * _m.pi)
    
    # Calculate the 
    def area(self):
        return (_m.pi * (self.radius)**2)


circle1 = Circle(float(input("Please input the radius of a Circle you want to calculate for: ")))


print("The circumference of a circle with raduis {} is {}".format(circle1.radius,circle1.circumference()))
print("The area of a circle with raduis {} is {}".format(circle1.radius,circle1.area()))
