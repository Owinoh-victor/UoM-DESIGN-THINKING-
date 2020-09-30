#Define Conversion class
class MetricConversion:
    #constructor
    def __init__(self, NewValue):
        self.__measurement = NewValue
        self.__celsius = float()
        self.__meters = float()
        #These next two lines call both DetermineCelsiius and DetermineMeters from the constructor
        #This way we don't have to include more code in main().
        #Additionally pay attention to how I needed to specify arguments when calling from
        #within the constructor.  I didn't have to do this when calling this method from main()
        self.DetermineCelsius(self.__measurement, self.__celsius)
        self.DetermineMeters(self.__measurement, self.__meters)

    #Notice how I needed to include parameter in my function definition statement.
    def DetermineCelsius(self,__measurement, __celsius):
        self.__celsius = (5/9)*(self.__measurement - 32)
    #Notice how I needed to include parameter in my function definition statement.
    def DetermineMeters(self, __measurement, __feet):
        self.__meters = self.__measurement * 0.305

    #Access methods to allow the program to use meters, celsius and measurement
    def ReturnCelsius(self):
        return self.__celsius

    def ReturnMeters(self):
        return self.__meters

    def ReturnMeasurement(self):
        return self.__measurement

def GetChoice():
    #Declare local variables
    choice = str()
    #Display the menu of choices
    DisplayMenu()
    #Ask the user for their choice and make sure it is a C, M or E
    while choice != "C" and choice != "M" and choice != "E":
        choice = input("What would you like to do?     ")
        #converts whatever they entered to upper case
        choice = choice.upper()
    return choice
def GetMeasureCelsius():
    #Needed a different validation function since we can allow for negative values
    #Declare local variables
    ValNumber = float()
    StringNumber = str()
    flag = False
    #Ask the user for farenheit and make sure it is a float.  If not ask the user
    #for another value
    StringNumber = input("Enter degress Farhenheit:  ")
    while flag == False:
        try:
            ValNumber = float(StringNumber)
            flag = True
        except ValueError:
            flag = False
            #Getting a better number since the user did not give me one.
            StringNumber = input("You did not enter a number.  Please try again:  ")

    #Now that we know we have a good number we can return it to main for further processing
    return ValNumber

def GetMeasureMeters():
    #This function validates feet to make sure it is a positive float
    #Declare local variables
    ValNumber = float()
    StringNumber = str()
    flag = False
    #Ask user for a value and then validate it
    #I am putting this into a string so that I don't get a bunch a read with the user enters letters.
    StringNumber = input("Enter feet:  ")
    while flag == False:
        try:
            ValNumber = float(StringNumber)
            #Checking to make sure I have a positive number
            if ValNumber > 0:
                flag = True
            else:
                flag = False
                #getting a better number since the user gave me a negative one.
                StringNumber = input("You did not enter a positive number.  Please try again:  ")
        except ValueError:
            flag = False
            #getting a better number since the user didn't even give me a number.
            StringNumber = input("You did not enter a number.  Please try again:  ")

    return ValNumber

def DisplayMenu():
    #This function just prints the menu.  Nothing more.  It is a non value returning function
    print("********************************************")
    print("Here are your conversion choices:")
    print("\t\tC..........To convert Farenheit to Celsius")
    print("\t\tM..........To convert Feet to Meters")
    print("\t\tE..........To Exit the program")
    print("********************************************")
    print()
            
def main():
    #Declare Variables
    UserMeasure = 0.0
    UserChoice = str()
    #Get the User's Choice on what they want to do
    UserChoice = GetChoice()
    #Convert Measurement
    while UserChoice == "C" or UserChoice == "M":
        if UserChoice == "C":
            #Get the measurement
            UserMeasure = GetMeasureCelsius()
             #Create the object
            NewConversion = MetricConversion(UserMeasure)
            #Display the results of the conversion
            print(NewConversion.ReturnMeasurement(), " degrees Fahrenheit converts to ", format(NewConversion.ReturnCelsius(), '.2f'), " degrees Celsius")
        else:
            #Get the measurement
            UserMeasure = GetMeasureMeters()
             #Create the object
            NewConversion = MetricConversion(UserMeasure)
            #Display the results of the conversion
            print(NewConversion.ReturnMeasurement(), " feet converts to ", format(NewConversion.ReturnMeters(), '.2f'), " meters")
        UserChoice = GetChoice()

    #Display a message to the user telling them the program is over
    print("***************************************")
    print("Thank you for using my program!")
        
    
main()









    
