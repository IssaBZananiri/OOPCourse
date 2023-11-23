'''
Calculator From String
Author: Issa B. Zananiri
Date: 23/11/2023
'''


class Calculator:
    
    # initialize the instance
    def __init__(self, stringos):
        self.stringos = stringos
    
    # Parse the String, so that we know what we need.
    def parser(self):
        self.num1, self.operator, self.num2 = self.stringos.split(" ")
        self.num1 = int(self.num1)
        self.num2 = int(self.num2)
    # Calculate according to the product thing
    def calculate(self):
        print(self.stringos)
        self.parser()
        if self.operator == "+":
            return (self.num1 + self.num2)
        elif self.operator == "-":
            return (self.num1-self.num2)
        elif self.operator == "*":
            return (self.num1 * self.num2)
        else:
            try:
                return(self.num1 / self.num2) 
            except ZeroDivisionError as e:
                print("I cannot Divide by Zero")


calculate1 = Calculator(input("Please Enter the numbers and Operations you need:"))
print("The answer is: {}".format(calculate1.calculate()))