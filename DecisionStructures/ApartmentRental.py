#Apartments Rental office program 

#welcome message
print ("Welcom to your new apartment")

#Decliare Variables
onebedroom = 625
twobedroom = 700
tenantname = ""
tenantmincome = ""
tenantmincomeint = 0
cosignername = ""
Cosignermincome = 0
amendedmonthly = 0
flag = 0
flag2 = 0

flag = input (print ("Choose from the following.. (1) One Bed Room = $ 625.00 monthly     (2) Two Bed Rooms = $700.00 monthly [Enter Number 1 or Number 2]"))
tenantname = input ("Enter Tenant's Name ")
tenantmincome = input ("Enter tenant's monthly income ")
if flag == 1:
    tenantmincomeint = tenantmincome
    amendedmonthly = onebedroom * 4
    if tenantmincomeint >= amendedmonthly:
        print ("congrats ", tenantname ," you will be able to rent this apartment")
    else:
        flag2= input("Sorry.. your monthly income dosen't support you!! you need more income!! Do you have a cosigner that can help you?  (yes) or (no)  ")
        if flag2 == "yes":
            cosignername = input ("Enter Cosigner Name ")
            cosignermincome = input ("Enter Cosigner Monthly Income ")
            if cosignermincome+tenantmincome >= (onebedroom*4):
                print ("congrats ", tenantname," Finaly you will be able to rent this apartment with the help of your cosigner ", cosignername)
            else:
                print ("Sorry.. your both monthly income dosen't support you!! you need more income")
                print ("Get another cosigner with more income and try again later")
        else:
            print ("sorry ", tenantname," you can'r rent this apartment")
else:
    tenantmincomeint = tenantmincome
    amendedmonthly = twobedroom * 4
    tenantmincomeint >= amendedmonthly
    print ("congrats ", tenantname ," you will be able to rent this apartment")
    if flag2 == input("Sorry.. your monthly income dosen't support you!! you need more income!! Do you have a cosigner that can help you?  (yes) or (no)  "):
        if flag2 == "yes":
            cosignername = input ("Enter Cosigner Name ")
            cosignermincome = input ("Enter Cosigner Monthly Income ")
            if (cosignermincome+tenantmincome) >= (twobedroom*4):
                print ("congrats ", tenantname," Finaly you will be able to rent this apartment with the help of your cosigner ", cosignername)
            else:
                print ("Sorry.. your both monthly income dosen't support you!! you need more income")
                print ("Get another cosigner with more income and try again later")
    else:
        print ("sorry ", tenantname," you can'r rent this apartment")
        
    
