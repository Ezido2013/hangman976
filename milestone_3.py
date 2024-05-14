import random

# Welcome to the game
print("Welcome to Hangman")
print("Try to guess a letter")

#secret words in list
word_list = ['apple', 'grapes', 'cherries', 'kiwi', 'oranges']
random_word = random.choice(word_list)

# Main loop
        
def check_guess(guess):
    guess = guess.lower()   
#checks if the letter you input is in the random generated word  
    if guess in random_word:             
        print("Good guess! {} is in the word". format(guess))
# else guess not in guess_list:         
    else:
        print("Sorry, {} is not in the word. Try again".format(guess))
        
def ask_for_input():     
#repeatedly asks you to guess the letter in a random word
    while True:                                     
        guess = input("Guess a letter:  ")
    # guess = guess.lower()

#checks if guess is a letter
        if guess.isalpha() == False:
            print("Invalid letter. Please enter a single alphabetical character")
        else:
            break       # breaks out of the loop
    check_guess(guess)
ask_for_input()