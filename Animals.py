# A program to do animals and specific ones properties
# Issa B. Zananiri
# Written: 11/11/2023
#

class Animal:
    def __init__(self, animal_name, legs, fur):
        self.animal_name = animal_name
        self.legs = legs
        self.fur = fur

    
    def print_animal(self, personal_animal_name):
        print("{} is a {} and it has {} legs and {} fur".format(personal_animal_name, self.animal_name, self.legs, self.fur))


class Dog(Animal):
    def bark_if_dog(self):
        if self.animal_name == "dog":
            print("Woof, Woof!!!")
        else:
            pass


# Now try to instantiate the Animal
my_animal = Dog("dog", 4, "long")
my_animal.print_animal("Meemo") 
my_animal.bark_if_dog()

