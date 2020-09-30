#This program demonstrates how to create a class in Python.
#It utilizes the Cube class example from the text

class Cube:
    def __init__(self, NewSide):
        self.__side = NewSide
        self.__volume = 2.0
#Method to calculate the volume
    def calvolume(self):
        self.__volume = self.__side**3

#Method to return side to main()
    def get_side(self):
        return self.__side

#Method to return volume to main()
    def get_volume(self):
        return self.__volume

#Create a new class Squarebox that inherits cube
class Rectangle(Cube):
    def __init__(self, NewSide, NewHeight):
        Cube.__init__(self, NewSide)
        self.__height = NewHeight
        self.__side = NewSide
        
#Method to calculate the volume of the square with different size sides
    def calvolume(self):
        self.__volume = self.__side**2 * self.__height

#Method to return height to main()
    def get_height(self):
        return self.__height

def GetShape():
    #Declare local variables
    selection = "nothing"
    print("What kind of shape do you want to calculate the volume for?")
    print("     Select from the menu below:")
    print("            S = Square (all sides are equal)")
    print("            R = Rectangle (2 sides are of different lengths")
    print("            E = Exit program")
    print()
    selection = input("Your Shape:  ")

    return selection

def DetSquareVol():
    #Declare local variables
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

def DetRectangleVol():
    #Declare local variables
    UserHeight = 0
    UserSide = 0

     #Ask the user for the width of the box.
    UserSide = int(input("Enter the width of your rectangle:  "))
    #Ask the user for the height of the box.
    UserHeight = int(input("Enter the height of your rectangle:  "))
    
    #Create a new object based off of the Cube Class
    my_rectangle = Rectangle(UserSide, UserHeight)

    #Generate the volume
    Rect_volume = my_rectangle.calvolume()
    print(Rect_volume)

    #Print out the side and volume
    print("You entered the width:  ", my_rectangle.get_side())
    print("You entered the height:  ", my_rectangle.get_height())
    print("The volume is:  ", my_rectangle.get_volume())

#The main program
def main():
    #Declare variables
    ShapeChoice = "nothing"
 #Ask the user what kind of shape they need to calculate the volume for
    ShapeChoice = GetShape()
    ShapeChoice = ShapeChoice.upper()

    while ShapeChoice == "S" or ShapeChoice == "R":
        #Determine what class to use
        if ShapeChoice == "S":
            DetSquareVol()
        else:
            DetRectangleVol()
         #Ask the user what kind of shape they need to calculate the volume for
        ShapeChoice = GetShape()
        ShapeChoice = ShapeChoice.upper()

#call Main
main()
