""""
3 functions
   MonthlyPremium()
    get rates
   monthlyBill()
    get total; bill
   main()
    get user input
    call all the three functions
    return all the function outputs

"""


basic=int()
sports=int()
movie=int()
kids=int()
def Monthlypremium():
    box = int()
    basic = int()
    sports = int()
    movie = int()
    kids = int()

    sports= 25
    movie=15
    kids= 10
    basic = 50

    if box ==1:
        type - str(input("Which package do you want: "))
    elif box ==2:
        for i in range (0,1):
            type - str(input("Which package do you want: "))
    elif box ==3:
        for i in range (0,2):
            type - str(input("Which package do you want: "))
    else:
        print ("None")


def  monthlyBill():
    type = str()
    if type =="sports":
         Bill= basic + sports
    elif type =="movie":
        Bill = movie + basic
    elif type=="kids":
        Bill= basic + kids
    elif type==" sports" and type=="movie" and type =="kids":
        Bill = basic + sports + movie + kids
    else:
        Bill = basic

    return Bill()
    print ("Total Bill:", Bill)

def main():

    box=int(input("Enter the number of boxes You want: "))

    Monthlypremium()
    monthlyBill()

main()
