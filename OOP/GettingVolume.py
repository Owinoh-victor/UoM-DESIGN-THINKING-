##################################################
#
#  Superclass: ThreeDimensionalShape
#
##################################################
class ThreeDimensionalShape(object):
    def __init__(self, name):
        self.__name = name

    def getShapeName(self):
        return self.__name

    def calculateVolume(self):
        print ('Hello')
    
################
# Derived class
################
class Cube(ThreeDimensionalShape):
    def __init__(self, name, side):
        ThreeDimensionalShape.__init__(self, name)
        self.__side = side

    def getSide():
        return self.__side

    def calculateVolume(self):   
        return self.__side**3


################
# Derived class
################
class Cylinder(ThreeDimensionalShape):
    def __init__(self, name, height, radius):
        ThreeDimensionalShape.__init__(self, name)
        self.__height = height
        self.__radius = radius

    def getHeight():
        return self.__height

    def getRadius():
        return self.__radius

    def calculateVolume(self):
        print(self.__name)
        return 3.1415 * self.__height * (self.__radius * self.__radius)

CUBE = 1
CYLINDER = 2
QUIT = 3

def main():

    selection =0

    while selection != QUIT:
        print ()
        displayMenu()
        print ()
        selection = int(input('Please enter your selection: '))

        if selection == 1:
            side = float(input('Please enter the lengh of a side: '))
            cube = Cube("Cube", side)
            print ('The volume of the cube is: ', str(cube.calculateVolume()))

        elif selection == 2:
            height = float(input('Please enter the height of the cylinder: '))
            radius = float(input('Please enter the radius of the cylinder: '))
            cylinder = Cylinder("Cylinder", height, radius)
            print ('The volume of the cylinder is: ', str(cylinder.calculateVolume()))

        elif selection == 3:
            print ('Thank you!')

def displayMenu():
    print ('Please select a 3D shape to calculate:')
    print ('1 - The volume of a Cube')
    print ('2 - The volume of a Cylinder')
    print ('3 - QUIT')

main()
