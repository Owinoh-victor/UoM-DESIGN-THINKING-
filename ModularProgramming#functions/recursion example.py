#Recursion Example

def CalculateSum(int_num):
    #local variables
    sum_num = int()
    if int_num == 1:
        sum_num = 1
    else:
        int_num = int_num - 1
        sum_num = CalculateSum(int_num)
        sum_num = sum_num + int_num
    #end if
    #return sum_num back to main()
    return sum_num
def main():
    #local variables
    my_num = int()
    new_num = int()
    user_continue = str()

    #loop that allows us to see what is going on
    while user_continue != 'q':
        my_num = int(input("Enter a number:  "))
        #call to CalculateSum function
        new_num = CalculateSum(my_num)
        #printing new_num
        print(new_num)
        #ask user to continue
        user_continue = input("Enter q to quit:  ")

main()

    
