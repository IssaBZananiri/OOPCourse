# Issa B. Zananiri
# Object Oriented Programming Course
# Camel Case for Class Names, starting with capital
import math
import turtle

class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_corrdinate = y
    
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x_coordinate < upright[0] and lowleft[1]<self.y_corrdinate <upright[1]:
            return True
        else:
            return False
    
    def distance(self, point):
        distanco = math.sqrt((point.x_coordinate-self.x_coordinate)**2 + (point.y_corrdinate-self.y_corrdinate)**2)
        print("The answer for this problem is = {}".format(distanco))


point1 = Point(5, 5)
point2 = Point(1,2)
point1.distance(point2)

