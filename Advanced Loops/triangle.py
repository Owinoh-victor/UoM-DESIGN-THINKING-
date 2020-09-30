""""
Problem
Create a program in Python that will draw a series of triangles. The program needs to ask the user for the number of triangles
 to draw and the size of the triangle.
The inputs for this program need to look like the following. After the colon there are no spaces.
Number:
Size:
Using these two inputs, your program will then draw a series of triangles in the size the user wishes.
For example if the user enters 3 triangles with a size of 5, the following will be the output:
*
**
***
****

*
**
***
****

*
**
***
****
The easiest way to solve this problem is with two loops. One loop draws the triangles and the other repeats the drawing.
When testing your program make sure you test with different sizes and different numbers of triangles as
this will be how your code will be run by Codio.
"""

#Declaire variables

#number = int()
size = int()
char= str()
#number = int(input("Number:"))
size = int(input("Size:"))

char= str(input())
def draw():

    #for n in range(0, number):
        for i in range(0, size):
            for j in range(0, i+1):
                print(char, end="")
            print()
draw()