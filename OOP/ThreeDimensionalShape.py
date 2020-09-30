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
        return None
    
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
        return 3.1415 * self.__height * (self.__radius * self.__radius)











