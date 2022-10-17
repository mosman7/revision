import random

def get_choices():
    player_choice = input("Enter choice")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player} computer chose {computer}")
    if player == computer:
        return "Its a tie, play again"
    elif player == "rock":
        if computer == "scissors":
            return "player wins"
        else:
            return "computer wins"
    elif player == "scissors":
        if computer == "paper":
            return "player wins"
        else:
            return "computer wins"
    elif player == "paper":
        if computer == "rock":
            return "player wins"
        else:
            return "computer wins"

choices = get_choices()
winner = check_win(choices["player"], choices["computer"])
print(winner)

def username():
    name = input("username:")
    return name
username()
print("your name is" username())