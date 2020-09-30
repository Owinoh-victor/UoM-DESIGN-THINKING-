#declare variable
Fahrenheit=()

#CONVERTION
while Fahrenheit != "Q" :
  Fahrenheit = float(input("Degrees Fahrenheit: "))
  Celsius = (Fahrenheit - 32) * 5 / 9
  print(" Degrees Celsius: ", Celsius)
  print("Continue: ")
  quit=str(input(" Enter Q to quit"))


