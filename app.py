# Author: William Dimaculangan

import random

def get_player_move():
    moves_list = ["Rock", "Paper", "Scissors"]
    valid_choices = ['1', '2', '3']
    while True:
        print("\n[1] Rock [2] Paper [3] Scissors\n")
        player_choice = input("Choose your weapon: ")

        if player_choice in valid_choices:
            return moves_list[int(player_choice)-1] # Return move based on index
        print("\nChoose a valid option to play this game.")

    
def get_computer_move():
    moves_list = ["Rock", "Paper", "Scissors"]
    move = random.choice(moves_list)
    return move

def score(player_name, player_score, computer_score):
    print("\nScore board:")
    print(f"Computer Score: {computer_score}")
    print(f"{player_name} Score: {player_score}")
    pass

def ask_play_again():
    valid_choices = ["y", "n"]
    while True:
        choice = input("Play Again? (Y/N): ")
        choice = choice.lower()
        if choice in valid_choices:
            if choice == "y":
                return True
            else: 
                return False
        print("Choose a valid option to play this game.")

def winner(player_name, player_score, computer_score):
    if player_score > computer_score:
        print(f"Congrats {player_name}, You won the game!")
    elif computer_score > player_score:
        print("The computer won the game. Try again next time!")
    else:
        print("It's a tie! You are both winners <3")

player_score = 0
computer_score = 0
play_again = True

print("Welcome to Rock Paper Scissors Game!\n")
player_name = input("Enter Player's Name: ")


while play_again:
    player_move = get_player_move()
    computer_move = get_computer_move()
    print(f"Computer chose: {computer_move}")
    print(f"{player_name} chose: {player_move}")
    if player_move == computer_move:
        print("IT'S A TIE!")
    elif (player_move == 'Rock' and computer_move == "Scissors") or \
         (player_move == 'Scissors' and computer_move == "Paper") or \
         (player_move == 'Paper' and computer_move == "Rock"):
        print(f"{player_name.upper()} WINS!")
        player_score += 1
    else:
        print("COMPUTER WINS!")
        computer_score += 1
    
    score(player_name, player_score, computer_score)
    play_again = ask_play_again()

winner(player_name, player_score, computer_score)

# Need more proper documentation, add more comments (multi-line) what the functions do and the parameters
'''
If you are deployed in projects clients can be strict on the requirements
 e.g. Using only two functions
'''