"""
Make a two-player Rock-Paper-Scissors game. 

Hint:
Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game
"""

p1 = 0
p2 = 0

def Game():
    print("Welcome to Rock-Paper-Scissors game!")
    print("1) Rock")
    print("2) Paper")
    print("3) Sissors")
    #print("4) Lizard")
    #print("5) Spock")
    
    P1_input()
    P2_input()
    GameComparison()
    #NewGame()

def P1_input():
    global p1
    p1 = int(input("P1 Enter your option "))
    if (p1 > 3 or p1 < 1):
        print("Sorry P1, invalid option. Try again.")
        P1_input()

def P2_input():
    global p2
    p2 = int(input("P2 Enter your option "))
    if (p2 > 3 or p2 < 1):
        print("Sorry P2, invalid option. Try again.")
        P2_input()

def GameComparison():
    if (p1 == 1 and p2 == 1):
        print("It's a tie")
    elif (p1 == 1 and p2 == 2):
        print("Congratulations P2, you won!")
    elif (p1 == 1 and p2 == 3):
        print("Congratulations P1, you won!")
    elif (p1 == 2 and p2 == 1):
        print("Congratulations P1, you won!")
    elif (p1 == 2 and p2 == 2):
        print("It's a tie")
    elif (p1 == 2 and p2 == 3):
        print("Congratulations P2, you won!")
    elif (p1 == 3 and p2 == 1):
        print("Congratulations P2, you won!")
    elif (p1 == 3 and p2 == 2):
        print("Congratulations P1, you won!")
    elif (p1 == 3 and p2 == 3):
        print("It's a tie")
    opc = int(input("Play again? (Type 1 to play again) " ))
    if (opc == 1):
        Game()
    else:
        print("Thanks for playing")
Game()