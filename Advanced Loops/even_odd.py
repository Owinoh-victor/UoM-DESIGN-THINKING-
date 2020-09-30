"""
Even & Odd
Create a program in Python that will accept a positive integer from the user and determine if that number is even or odd.
The program will keep asking the user for a number until they enter Q for quit. When a number is determined to be even or odd,
the program needs to print that to the screen.
The input prompt for the number does not need a prompt. Therefore your Python code will look like the following:
num = int(input())
The input prompt for the question asking the user if they wish to continue will look like:
Continue:
With no spaces after the colon.
When a number is judged to be even the program needs to print:
even
When a number is judged to be odd the program needs to print:
odd
"""
answer = str()
num = int()
modulo=int()
while answer != 'Q':
    num = int(input())
    modulo= num % 2
    if modulo ==0:
        print ("even")
        print("Continue:")
    else :
        print("odd")
        print("Continue:")
# ask the user if they want to enter another batch
    answer = input("")


