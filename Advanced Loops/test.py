# variable
Fahrenheit = float()

# user input
Fahrenheit = float(input())


# function
def GetCelsius():
    degrees_celsius = (Fahrenheit - 32) * 0.5556

    # conversion into int
    degrees_celsius = int(degrees_celsius)

    return degrees_celsius


# function call
GetCelsius()