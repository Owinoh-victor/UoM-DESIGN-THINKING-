
def  RainFall(days):
    mylist = []
    for i in range (days):
        rain = int(input("Enter Amount f rainfall:"))
        mylist.append(rain)

    return mylist


def main():
    days=int()

    days=int(input("How many days of rainfall:"))

    mylist=RainFall(days)
    print(mylist)

main()