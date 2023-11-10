# Issa B. Zananiri
# Object Oriented Programming Course
# Camel Case for Class Names, starting with capital
import math
import turtle
from random import randint

class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_corrdinate = y
    
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft.x_coordinate < self.x_coordinate < upright.x_coordinate and lowleft.y_corrdinate<self.y_corrdinate<upright._corrdinate:
            return True
        else:
            return False
    
    def distance(self, point):
        distanco = math.sqrt((point.x_coordinate-self.x_coordinate)**2 + (point.y_corrdinate-self.y_corrdinate)**2)
        print("The answer for this problem is = {}".format(distanco))


class Recatangle:
    def __init__ (self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point1.x_coordinate - self.point1.x_coordinate) * (self.point2.y_coordinate - self.point2.y_coordinate)
    

class GuiRectangleClass(Recatangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x_coordinate,self.point1.y_corrdinate)

        canvas.pendown()
        canvas.forward(self.point1.x_coordinate-self.point2.x_coordinate)
        canvas.left(90)
        canvas.forward(self.point1.y_corrdinate-self.point2.y_corrdinate)
        canvas.left(90)
        canvas.forward(self.point1.x_coordinate-self.point2.x_coordinate)
        canvas.left(90)
        canvas.forward(self.point1.y_corrdinate-self.point2.y_corrdinate)
        canvas.done()
              
class GuiPoint(Point):
    def draw(self,canvas):
        canvas.up()
        canvas.setpos(self.x_coordinate, self.y_corrdinate)
        canvas.down()
        canvas.dot(self.x_coordinate, self.y_corrdinate)

        canvas.done()



my_turtle = turtle.Turtle()

# Create a canvas Instance
rectangle = GuiRectangleClass(Point(randint(0,100),randint(0,100)),Point(randint(0,100),randint(0,100)))
rectangle.draw(my_turtle)
print ("Rectangle Coordinates: ", rectangle.point1.x_coordinate, ",", rectangle.point1.y_corrdinate, "and " , rectangle.point2.x_coordinate, ",", rectangle.point2.y_corrdinate)
user_point = GuiPoint(float(input("Guess x:")), float(input("Guess y:")))
user_area = float(input("Please Guess the Area"))

#user_point.draw(my_turtle)

print("Your point was inside a rectangle: ", user_point.falls_in_rectangle(rectangle.point1, rectangle.point2))
