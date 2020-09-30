somenumber = 1 #Global variable which is VERY bad -- don't do this
               #unless it is a constant

#notice the order of the functions with def main() at the bottom
#     this is a Python 2.x thing

#notice the definition of the parameter a_number.  Parameters do not
#     have to be named the same as their arguments.

def DetermineX(a_number):
    total_num = int()
    your_num = int()

    your_num = int(input("Enter a number:  "))

    total_num = your_num + a_number + somenumber

    print("total_num = ", total_num)

def main():
    #Declare variables
    local_main = int()  #local variable to main
    local_mainTwo = int()

    #local variables in main can be shared but need to be passed into
    #the function

    #Give local main a value
    local_main = 3
    
    DetermineX(local_main)#This is a call statement when our function
                          #is not returning a value
    
    print(somenumber)

    print("Value of local_main:  ", local_main)

    #Call our function a second time, this time sending in a different
    #variable
    local_mainTwo = 5
    DetermineX(local_mainTwo)
    print("Value of local_main:  ", local_mainTwo)    

    #print(total_num)

main()  #must call main() in order for your code to work
