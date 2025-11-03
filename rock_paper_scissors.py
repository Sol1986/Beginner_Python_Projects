import random

player_score = 0
computer_score = 0

# Mapping of choices
choice = {
    "Rock🪨": 0,
    "Paper🗞️": 1,
    "Scissor✂️":2
}
# Function for computer's random choice
def computer():
    key, value = random.choice(list(choice.items()))
    return key,value

# Function to play a round
def play(p_score, c_score):

    player_move_number = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if player_move_number not in [0,1,2]:
        print("Invalid input. Please enter 0, 1, or 2.")
        return p_score, c_score
    
    player_move_name = [name for name, number in choice.items() if number == player_move_number][0]

    computer_move_name,computer_move_number = computer()

    print (f"You chose {player_move_name}")
    print (f"I chose {computer_move_name}")


    if player_move_number == computer_move_number:
        print ("Ahh... it's a tie!")
    elif player_move_number  == 0 and computer_move_number==1:
        print ("Haha I win! 😝")
        c_score += 1
    elif player_move_number  == 0 and computer_move_number==2:
        print ("Nice! You win! 🏆")
        p_score +=1
    elif player_move_number  == 1 and computer_move_number==0:
        print ("Nice! You win! 🏆")
        p_score +=1
    elif player_move_number  == 1 and computer_move_number==2:
        print ("Haha I win! 😝")
        c_score +=1
    elif player_move_number  == 2 and computer_move_number==0:
        print ("Haha I win! 😝")
        c_score +=1
    elif player_move_number  == 2 and computer_move_number==1:
        print ("Nice! You win! 🏆")
        p_score +=1
    else:
        print("wrong_input")
    return p_score, c_score

# Main game loop
while True:
    player_score,computer_score =play(player_score, computer_score)
    print (f"Current Score-> You: {player_score}, Me: {computer_score}")
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break


