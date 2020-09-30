

myword = "PYTHON"

myletter = myword[3]

print(myletter)

myword = "PYTHON"
index = int()

for index in range (0, 6):
    if myword[index] == "O":
        print("We found your letter")
        print(index)
        break

if index == 6:
    print("Sorry we did not find your letter")
            


