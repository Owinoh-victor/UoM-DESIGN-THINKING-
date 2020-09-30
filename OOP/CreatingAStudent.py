class Student:
  

   def __init__(self, name, grade):
      self.name = name
      self.grade = grade

   def displayStudent(self):
      print "Name : ", self.name,  ", Grade: ", self.grade


student1 = Student("Mike", 7)
student2 = Student("Julie", 8)
student1.displayStudent()
student2.displayStudent()


## This program is going to display a list of students and the grade they belong
## to using a class with a constructor and a method.
## I will break the code down by each line and explain whats going.

##Line1: You begin by declaring the name of the class. It can be anything, but
##  it is best to name it something revelant to purpose the of the program. So I
##  will name mine Student. The syntax is the keword "class" then the name of
##  the class you wish to give it and ended with a colon(:).
## Also declare all your variables after the class name

##Line4: Next we build the contructor. A contructor gives default values to an
##  object. For example this program wants to display the names and grades of
##  students. If we already know the names of the students and the grade they
##  are in, we can initialize or provide a value for those objects. So in this
##  case we know the names and grades so we build a constructor. The required
##  syntax is "def_init__(self,". Following the comma are the values you want
##  the default value for. These are called arguements and are separated by commas.
##  In this example the arguments are "name" and "grade". So the contructor is
##  "def_init__(self, name, grade). These arguments don't have to be name
##  and grade, they can be anything, but it helps make the program more
##  readible if you name them purposefully.
##  Also note that the constructor is only used if want default
##  values. You can skip it entirely and just request the values to be
##  inputted by the user.

##Line5 & Line6: These two lines are like assigning default values to variables
##  like you did during the semester.
##  Except you are assigning the default values of the
##  constructors arguments to the new varibles that are used in the program later.
##  In this case the variables are self.name and self.grade and they are set
##  equal to whatever the default values of the arguements name and grade
##  will be. Its good to use "the argument name as the variable for readablity,
##  but remember to use "self.argument name" and then assign it to the arguement
##  name. So in this example its "self.name = name"

##Line8: Next create a method whose purpose it is to display the name and
##  grade of the student. The syntax of creating a method is the same as the
##  constructor except we don't require any additional arguments. In this
##  example we gave the method the name displayStudent because that is what
##  we want the program to do. However you can name the method anything you
##  wish.

##Line9: We give the method instructions on what do to. We want to output
##  the student name and grade. So the method outputs the name and the grades
##  The students name and grade are going to be stored into the
##  self.name and self.grade varible

##Line12: In order to use the methods of a class you have to be able to call
##  that method
##  by creating an object of that method. An object works like a variable.
##  You put things inside of it for later use. So we create the object(variable)
##  student1 to put the constructor of the Student class inside of
##  student1. So we use the name Student. In the parenthesis goes your
##  predetermined values for arguement that you choose for contructor.
##  In this example I choose the name Mike and decided he was in the 7 grade.
##  If the number of arguements in your object declaration 
##  does not match with the number of arguements in the contructor, 
##  it results in a compilation error. For example if you just put one value
##  inside the parenthesis, it would result in an error because the constructor
##  asked for a name and grade. So the number arguements have to match.

##Line13: This creates another object for a second student and stores it in
## student2. You can create as many objects as you want. However you can also
##  just put it in a loop to save you a lot of typing. Imagine if you had
##  600 students you would not want to create a seperate object for all 600
##  students. That is way too much typing. Just create an array and store an
##  object of students in it and loop through the array as many times as you need

##Line14 & 15: We have the displayStudent method to
##  display the output of students. We have created the objects to call our
##  methodsl. Use the name your object, a
##  period, then the name of the method and its arguements. If there are no
##  arguements leave the paranthesis empty.
##  So in this example its "student1.displayStudent()".
##                        objectname   method name

