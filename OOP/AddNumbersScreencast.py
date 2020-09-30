import random
class MathProblem:
    def __init__(self):
        self.num1 = int()
        self.num2 = int()
        self.sum = int()

    def GetNumbers(self):
        self.num1 = random.randint(0, 10)
        self.num2 = random.randint(0, 10)

    def AddNumbers(self):
        self.sum = self.num1 + self.num2

    def ReturnSum(self):
        return self.sum

myAddition = MathProblem()
myAddition.GetNumbers()
myAddition.AddNumbers()
print(myAddition.ReturnSum())
