import random

def get_choices():  # This function takes user input and selects a option for computer too.
    player_choice = input("Enter a choice (rock , paper , scissor): ")
    
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options) 
    
    choices = {"player" : player_choice , "computer" : computer_choice}
    return choices


def check_win(player , computer):   # This function checks if the player wins or looses.
    print(f"You choose {player} computer chose {computer}")

    if(player == computer):
        return "it is a Tie!!"
    elif player == "rock":
        if computer == "scissor":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut Paper! You lose."
      
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut Paper! You win!"
        else:
            return "Rock crushes Scissors! You lose."

choices = get_choices() # Choices are taken.
result = check_win(choices["player"] , choices["computer"]) # result is set using check_win;.l

print(result)
