# word list
import random

word_list = ["tiger", "monkey", "camel", "baboon"]

chosen_word = random.choice(word_list)

# print(chosen_word)

guess = input("Geuss a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")
