daysUnder100 = int()
daysUnder200 = int()
daysOver200 = int()
total_sales = float()
daily_sales = float()
days = int()
user_sales = str()

while user_sales == "yes" and days < 7:
    daily_sales = float(input("Enter today's sales:"))
    total_sales = daily_sales + total_sales
    if daily_sales < 100:
        daysUnder100 = 0
        daysUnder100 = daysUnder100 + 1
    elif daily_sales <= 200:
        daysUnder200 = 0
        daysUnder200 = daysUnder200 + 1
    else:
        daysOver200 = 0
        daysOver200 = daysOver200 + 1
    user_sales = input("Enter yes to keep tabulating sales:  ")
    print("------------------------------------")
    print("Total Sales:  ", total_sales)
    print("Days Under $100:  ", daysUnder100)
    print("Days Under $200:  ", daysUnder200)
    print("Days Under $300:  ", daysOver200)