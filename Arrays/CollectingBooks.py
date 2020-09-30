##Declare Variables
NumBooks = 0
Book = "nothing"
Books[] = 0
Index = 0
Number = 1


NumBooks = int(input("How many books are on your favorite book list?   "))
Books = [" "] * NumBooks

while Index < NumBooks:
    Book = str(input("Enter a favorite book of yours:   "))
    Books[Index] = Book
    Index = Index + 1
    
Index = 0
print("")
print("Your list of books")
print("******************************************")

while Index < NumBooks:
    print(Number,". ", Books[Index])
    Index = Index + 1
    Number = Number + 1
