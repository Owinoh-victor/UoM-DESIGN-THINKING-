#This program demonstrates how to create a class in Python.
#It utilizes the Cube class example from the text

class Cube:
    def __init__(self, NewSide):
        self.side = NewSide
        self.volume = 1.0
#Method to calculate the volume
    def calvolume(self):
        self.volume = self.side**3

#Method to return side to main()
    def get_side(self):
        return self.side

#Method to return volume to main()
    def get_volume(self):
        return self.volume


#The main program
def main():
    #Declare variables
    UserSide = 0

    #Ask the user to enter a side
    UserSide = int(input("Enter a side:  "))
    
    #Create a new object based off of the Cube Class
    my_cube = Cube(UserSide)

    #Generate the volume
    my_cube.calvolume()

    #Print out the side and volume
    print("You entered the side:  ", my_cube.get_side())
    print("The volume is:  ", my_cube.get_volume())


#call Main
main()
