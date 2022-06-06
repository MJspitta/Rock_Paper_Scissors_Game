import random

gameOptions = ['r', 'p', 's']
print("\nWelcome to the Rock-Paper-Scissors Game! \n R is for Rock. \n P is for Paper. \n S is for Scissors.\n")

while True:
    print("\nPlease make a selection from the options('R', 'P', 'S')")

    while True:
        playerSelection = str.lower(input("Player Selection: \n"))

        if playerSelection == 'r':
            playerPick = 'Rock'
            break
        elif playerSelection == 'p':
            playerPick = 'Paper'
            break
        elif playerSelection == 's':
            playerPick = 'Scissors'
            break
        else:
            print("\nInvalid option!!! Kindly make another selection!")
            continue

    computerSelection = random.choice(gameOptions)
    if computerSelection == 'r':
        computerPick = 'Rock'
    elif computerSelection == 'p':
        computerPick = 'Paper'
    elif computerSelection == 's':
        computerPick = 'Scissors'
    
    print("----------------------------------------------------------------------")
    print("Player (", playerPick,") : CPU (", computerPick,")\n")

    if playerSelection == computerSelection:
        print("The result is a DRAW! Try again!")
        continue
    elif (playerSelection=='r' and computerSelection=='p'):
        print("PAPER beats rock! YOU LOSE!")
    elif (playerSelection=='r' and computerSelection=='s'):
        print("ROCK beats scissors! YOU WIN!")
    elif (playerSelection=='s' and computerSelection=='p'):
        print("SCISSORS beats paper! YOU WIN!")
    elif (playerSelection=='p' and computerSelection=='r'):
        print("PAPER beats rock! YOU WIN!")
    elif (playerSelection=='s' and computerSelection=='r'):
        print("ROCK beats scissors! YOU LOSE!")
    elif (playerSelection=='p' and computerSelection=='s'):
        print("SCISSORS beats paper! YOU LOSE!")
    
    anotherRound = input("Would you like to play again? (y/n): ")
    if anotherRound.lower() != 'y':
        break
    