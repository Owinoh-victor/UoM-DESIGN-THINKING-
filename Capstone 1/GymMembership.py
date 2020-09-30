"""
7. Challenge Exercise 5 ~ Gym Membership
Create a class called GymMembership that takes in the number of Gym Memberships and the type. Using a constructor,
assign two attributes to the number of memberships and type. Within this class add three methods: DetermineRate,
 DetermineTotal and ReturnTotal. DetermineRate will find the cost of the membership based on the type of membership the user wants.
  It will store this value in the attribute rate. The “bronze” membership is 25 dollars a month, the “silver” membership is 35 dolars a month,
  the “gold” membership is 50 dollars a month and the “platinum” is 75 dollars a month.
  The method DetermineTotal will use the cost of one membership and multiply it by the number of memberships.
  It will store this value in an attribute called total. At this gym customers agree to a one year contract.
  Therefore the total is going to be for the year and not the month. Finally the ReturnTotal method returns the total cost for the membership.
When creating this class start coding in VS Code or IDLE. To test your class create an object. Send in the values 5 and silver.
Next call your method DetermineRate followed by DetermineTotal. Finally print the method ReturnTotal to the screen.
 Your code should print the following:
2100

"""
class GymMembership:
  def __init__(self, number_of_membership, member_type):
    self.membership = number_of_membership
    self.myType = member_type
    self.rate =int()
    self.Total =float()
    self.GetAll =int()


  def DetermineRate(self):
      if self.myType=="bronze":
          self.rate =25

      elif self.myType=="silver":
            self.rate =35

      elif self.myType=="gold":
            self.rate =50

      elif self.myType=="platinum":
            self.rate =75

      return self.rate

  def DetermineTotal(self):

      self.DetermineRate()
      self.Total = self.rate * self.membership * 12

      return self.Total

  def  ReturnTotal(self):
      return self.DetermineTotal()

def main():
    obj =GymMembership(5 ,"silver")
    obj.DetermineRate()
    obj.DetermineTotal()

    # output
    print (obj.ReturnTotal())

main()



