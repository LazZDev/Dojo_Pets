# Defined the Pet class
class Pet:
    # Initialized the Pet class with required attributes
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

# Defined the sleep method to increase energy by 25
    def sleep(self):
        self.energy += 25
        return self

# Defined the eat method to increase energy and health by 5 and 10 respectively
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

# Defined the play method to increase health
    def play(self):
        self.health += 5
        return self

# Defined the noise method to print a sound
    def noise(self):
        print("wooofff")
        return self


# Created a Pet instance called Buddy with the provided attributes
my_pet = Pet("Buddy", "Dog", ["sit", "fetch"], 100, 50)

# Called the noise method on the Buddy instance, which printed "wooofff"
my_pet.noise()
