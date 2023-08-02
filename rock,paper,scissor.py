import random



def get_choices():
    player_choice = input("Enter a choice (rock , paper , scissor): ")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options) 
    choices = {"player" : player_choice , "computer" : computer_choice}
    return choices

def check_win(player , computer):
    print(f"You choose {player} computer chose {computer}")
    if(player == computer):
        return "it is a Tie!!"
    
check_win("rock" ,"paper")
