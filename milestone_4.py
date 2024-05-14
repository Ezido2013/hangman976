import random
word_list = ["apple", "grapes", "cherries", "kiwi", "oranges"] 
guess = ''
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) 
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = -1
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [ ]    
        
#checks if the letter you input is in the random generated word  
    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:             
            print("Good guess! {} is in the word". format(guess))
            for i, letter in enumerate(self.word):
                # if letter != ["_"] and guess == letter:
                if letter == guess:
                    self.word_guessed[i] = letter
                else:
                    self.num_letters -= 1 
            print(' '.join(self.word_guessed))
                      
        else:
            self.num_lives -= 1 
            print("Sorry, {} is not in the word". format(guess)) 
            print("You have {} lives left". format(self.num_lives))
                 
# #repeatedly asks you to guess the letter in a random word   
    def ask_for_input(self):     
        while True:                                   
            guess = input("Guess a letter:  ")   
#checks if guess is a letter
            if guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
word = Hangman(word_list, num_lives=5)
word.ask_for_input()


