'''
Exercise 2: Create a Person with 
Date: 22/11/2023
A Class that creates a person and calculates its age
Author: Issa B. Zananiri
'''
from datetime import datetime, date


class Person:
    #initialize the instance of the person
    def __init__(self, first_name, last_name, country, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
    
    # Do the full name method
    def full_name(self):
        return (self.first_name +' '+self.last_name)
    

    # Calculate the Age of the Person
    def calculate_age(self):
        birthdate = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age



first_name = input("Please input the first name of the Person: ")
last_name = input("Please input the last name of the Person: ")
country = input("Please input the person country of birth: ")
date_of_birth = input("Please Enter the date of bireth YY-MM-DD: ")

person1 = Person(first_name, last_name, country, date_of_birth)
print("{} was born in {}, and he/she is Currently {} years old".format(person1.full_name(), person1.country, person1.calculate_age()))