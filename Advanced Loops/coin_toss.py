""""
Coin Toss
Create a program in Python that will mimic a coin toss.
The program needs to accept either heads or tails as possible values for a coin.
It will then count how many times heads is entered and how many times tails is entered.
When heads is entered it will display the message "Heads Win!". When tails is entered it will display "Tails Win!".
Additionally the program will keep running until the user enters Q to quit.
At the very end of the program it will print out the score for both heads and tails.
For this program you will need specific input prompts. When inputting the type of coin (heads or tails).
"""
answer = str()
Toss = str()
Heads_Score = int()
Tails_Score = int()
total_heads = 0
total_tails = 0
count = 0
while answer != 'Q':
    Toss = str(input("Toss:"))
    if Toss == "heads":
        print("Heads Win!")
        count = 0
        Heads_Score = count + 1
        total_heads = total_heads + Heads_Score
        print("Continue:")
    else:
        print("Tails Win!")
        count = 0
        Tails_Score = count + 1
        total_tails = total_tails + Tails_Score
        print("Continue:")

    # ask the user if they want to enter another batch
    answer = input("")
print("Heads Score:", total_heads)
print("Tails Score:", total_tails)




