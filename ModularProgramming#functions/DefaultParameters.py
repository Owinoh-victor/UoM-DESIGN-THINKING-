#Examples of using default parameter values

def GetDates(month = 'Jan', day = '1', year = '2016'):
    print('Dates Changed')
    print(month, '\t', day, '\t', year)

def main():
    #variables in main
    mymonth = str()
    myday = str()
    myyear = str()
    #testing function giving all three values
    print("Testing with all 3 values provided in the call")
    GetDates('November', '5', '2017')
    print()
    print("Testing with 2 values provided in the call")
    GetDates('October', '31')
    print()
    print("Testing with 1 value provided in the call")
    GetDates('September')
    print()
    print("Testing with no values given in the call")
    GetDates()

main()
