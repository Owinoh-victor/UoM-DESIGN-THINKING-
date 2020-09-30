x = 1
ConstantValue = "This is a constant"

def DetermineX():
    x = 2
    print(x)
    print(ConstantValue)
    return x


def main():
    x = DetermineX()
    print(x)
    print(ConstantValue)


main()
