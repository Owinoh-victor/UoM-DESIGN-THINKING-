#
# Polymorphism
#

class Pet:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print ("Hello, I'm a pet!")

class Dog(Pet):
    def speak(self):
        return ("Ruff, ruff!")

class Cat(Pet):
    def speak(self):
        return ("Meow, meow!")

class Parrot(Pet):
    def speak(self):
        return ("Pauly want a cracker?")
    
allMyPets = [Dog("Buck"),
             Cat("Oreo"),
             Cat("Honey"),
             Parrot("Pauly")]

for mypets in allMyPets:
    print (mypets.name , " is my name and I say " , mypets.speak())

    



