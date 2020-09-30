
class Bike:

    def _init_(self):
        self.tire s =str()
        self.colo r =str()
        self.num_speed s =int()

    def MoveForward(self):
        print("Moving Forward")

    def Brake(self):
        print("STOP")

    def TurnRight(self):
        print("Turning Right")

    def TurnLeft(self):
        print("Turning Left")

def main():
    # my object
    MyRedBik e =Bike()

    MyRedBike.colo r ='red'
    MyRedBike.tire s ='fat tires'
    MyRedBike.num_speed s =7

    # methord invocation
    MyRedBike.MoveForward()
    MyRedBike.TurnRight()
    MyRedBike.TurnLeft()
    MyRedBike.Brake()

    # output
    print(MyRedBike.color)
    print(MyRedBike.tires)
    print (MyRedBike.num_speeds)


main()