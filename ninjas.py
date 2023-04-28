# Imported the Pet class from the pets module
from pets import Pet

# Defined the Ninja class


class Ninja:
    # Initialized the Ninja class with required attributes
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# Defined the walk method (not yet implemented)
    def walk(self):
        pass

# Defined the feed method (not yet implemented)
    def feed(self):
        pass

# Defined the bathe method (not yet implemented)
    def bathe(self):
        pass

# Defined the pet_info method to display pet's information
    def pet_info(self):
        print(f"{self.pet.name} is a {self.pet.type} and is {self.pet.age} years old.")


# Defined a list of treats
treats = ["Bacon", "Chicken", "Peanut Butter"]
# Defined a list of pet food brands
pet_food = ["Purina", "Pedigree"]

# Created a Pet instance called Bela with the provided attributes
Bela = Pet("Bela", "Dog", 2, 100, 50)
# Created a Ninja instance called Laz with the provided attributes
Laz = Ninja("Laz", "C", treats[0], pet_food[0], Bela)
# Printed Laz's first name and their pet's name
print(Laz.first_name, Laz.pet.name)
