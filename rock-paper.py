from random import choice

def main():
    #get choice from the user
    choose = get_choice()
    #compare choice with computer
    winner = check_choice(*choose)
    #select the winner
    print(winner)

def get_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    while True:
        try:
            player_choice = input(str("choice: ")).capitalize()
            if player_choice in choices:
                break
        except ValueError:
            pass
    return [player_choice, computer_choice]
    
    

def check_choice(player_choice, computer_choice):
    print(f"You Choose {player_choice} and computer choose {computer_choice}")
    if player_choice == computer_choice:
        return "It A Tie"
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            return "Rock Beats Scissors, Player WIns!"
        else:
            return "Paper Beats Rock, Computer Wins!"
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            return "Paper Beats Rock, Player Wins!"
        else:
            return "Scissors Beats Paper, Computer Wins"
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            return "Rock Beats Scissors, Computer WIns!"
        else:
            return "Scissors Beats Paper, Player Wins"


if __name__ == "__main__":
    main()