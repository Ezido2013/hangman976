import random

def word_list():
    return word_list
word_list = ["Apple", "Grapes", "Kiwi", "Pear", "Banana"]
print(word_list)

word = random.choice(word_list)
print(word)
guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
