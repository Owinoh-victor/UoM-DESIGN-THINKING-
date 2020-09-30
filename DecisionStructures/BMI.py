# Example02 // by R.M. Weidner // My philosophy, like color television, is all there in black and white.

# This is the Python version of the Body Mass Index (BMI) program previously built in Raptor. Feel
# free to compare the two files to see what changes exist between the flow chart (Raptor) and the
# actual program (Python).

# Declaring Variables to be input by User

Height = int    # Notice that I'm now using 'int' to say this is an integer. I'm not giving a fixed value.
Weight = int
BMI = float     # Since the BMI value will have a decimal, I declared it as a float.

Weight = int(input("Please enter your weight in pounds:  "))
Height = int(input("Please enter your height in inches:  "))

BMI = (Weight * 703)/(Height**2)    # You'll notice that in Raptor, squaring a number used '^2', but
                                                                    # in Python it is a double asterisk.
                                                                    
# Okay, now we are going to look at what a decision tree looks like in Python.
# In the case below, it helps to read it as, "If BMI is less than 18.5, then
# do whatever is indented below that line. If that's NOT the case, then check if BMI is between 18.5
# and 24.9, and if it is then do whatever is indented below THAT line...")

if BMI < 18.5:
    print("Your Body Mass Index is ", format(BMI, '.2f'))       # I'm introducing a formatting option, 
    print("You are considered Underweight.")                     # using the 'format' command you see to
elif BMI >= 18.5 and BMI <= 24.9:                                            # the left. Doing this allows you to control
    print("Your Body Mass Index is ", format(BMI,'.2f'))        # just how many places past the decimal 
    print("You are considered Normal.")                                 # point the user actually sees displayed.
elif BMI >=25 and BMI <=29.9:
    print("Your Body Mass Index is ", format(BMI, '.2f'))
    print("You are considered Overweight.")
else:
    print("Your Body Mass Index is ", format(BMI, '.2f'))
    print("You are considered Obese.")
