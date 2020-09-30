#declare a global variable
score = 85
print("Global Variable score = ", score)
print()
def ChangeScore():
    #Checking on the value of score
    #print("Inside ChangeScore() BEFORE score is changed.")
    #print(score)
    #print()
    #changing the value of score
    score = 95
    print("Inside ChangeScore() AFTER score is changed")
    print(score)
    print()

def main():
    #changing the value of score
    ChangeScore()
    #Back to main
    #print("Back in main current value of score")
    #print(score)
    #Changing score again
    score = 100
    print("Inside main(), AFTER another change.")
    print(score)

main()

score = 50
print("Changing score again.")
print(score)
