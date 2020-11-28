import random

def RPS ():
    print("Rock Paper Scissors")
    playerInput = input("Rock, Paper or Scissors: ")
    #print(playerInput)

    gameChoice = random.randint(1,3)
    if gameChoice == 1:
        gameChoice = "Rock"
    elif gameChoice == 2:
        gameChoice = "Paper"
    else:
        gameChoice = "Scissors"

    won = "You won"
    lose = "You lost"
    draw = "You didn't lose but you didn't win either"


    if gameChoice == playerInput:
        print(draw)
    elif gameChoice == "Rock" and playerInput == "Paper":
        print(won)
    elif gameChoice == "Rock" and playerInput == "Scissors":
        print(lose)
    elif gameChoice == "Paper" and playerInput == "Rock":
        print(lose)
    elif gameChoice == "Paper" and playerInput == "Scissors":
        print(won)
    elif gameChoice == "Scissors" and playerInput == "Paper":
        print(lose)
    elif gameChoice == "Scissors" and playerInput == "Rock":
        print(won)
    print(gameChoice)
RPS()
