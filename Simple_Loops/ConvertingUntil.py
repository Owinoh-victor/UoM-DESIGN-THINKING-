#This program demonstrates how to convert an UNTIL loop to a WHILE loop

Name = "nothing"
Name = input("Enter the name of your brother or sister:  ")
while Name != "Done":
    print(Name)
    Name = input("Enter the name of your brother or sister:  ")

print("All Done")
