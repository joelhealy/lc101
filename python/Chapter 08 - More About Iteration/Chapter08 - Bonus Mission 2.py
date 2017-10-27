import random


def convert_number_to_rps(n):
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    else:
        return ""


def game(play1, play2):
    if play1 == play2:
        return "tie"
    elif play1 == "rock":
        if play2 == "scissors":
            return "win"
        elif play2 == "paper":
            return "lose"
        else:
            return "Illegal move - " + play2
    elif play1 == "paper":
        if play2 == "rock":
            return "win"
        elif play2 == "scissors":
            return "lose"
        else:
            return "Illegal move - " + play2
    elif play1 == "scissors":
        if play2 == "paper":
            return "win"
        elif play2 == "rock":
            return "lose"
        else:
            return "Illegal move - " + play2
    else:
        return "Illegal move - " + play1
    
    
def main():
    best_of = int(input("How many games do you want to play?  "))
    num_to_win = best_of // 2 + 1
    player_games_won = 0
    computer_games_won = 0
    while player_games_won < num_to_win and computer_games_won < num_to_win:
        print("\nStarting a new game")
        player = input("What is your play? (rock, paper or scissors):  ")
        computer = convert_number_to_rps(random.randrange(3))
        outcome = game(player, computer)
        if outcome == "win":
            print("You won this game.  The computer played '" + computer + "'.")
            player_games_won += 1
            print("The current score is You:", player_games_won,  \
                  " -  Computer:", computer_games_won)
        elif outcome == "lose":
            print("You lost this game.  The computer played '" + computer + "'.")
            computer_games_won += 1
            print("The current score is You:", player_games_won,  \
                  " -  Computer:", computer_games_won)
        elif outcome == "tie":
            print("Tie game.  The computer also played '" + computer + "'.")
            print("The current score is still You:", player_games_won,  \
                  " -  Computer:", computer_games_won)
        else:
            print("An invalid move was made.  This game doesn't count.")

    #  print out a message based on who won the match

    print(" ")
    if player_games_won > computer_games_won:
        print("Congratulations!  You beat the computer", player_games_won,  \
              "games to", computer_games_won)
    else:
        print("Better luck next time.  The computer beat you", computer_games_won,  \
              "games to", player_games_won)

            
if __name__ == "__main__":
    main()
    
