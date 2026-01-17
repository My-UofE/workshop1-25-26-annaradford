import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[len(poss_values)//2]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    return (current_val < next_val and user_input == "h") or \
           (current_val > next_val and user_input == "l")

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    correct = False
    for w_letter in enumerate(word):
        if w_letter[1] == letter:
            board[w_letter[0]] = w_letter[1]
            correct = True
    return correct
