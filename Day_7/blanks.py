import random

word_list = ["camel", "donkey", "sheep", "goat"]

choosen_word = random.choice(word_list)
print(choosen_word)

display = []
word_lenght = len(choosen_word)
for _ in range(word_lenght):
    display.append("_")
print(display)

# guess = input("Guess a letter: ").lower()

# for pos in range(len(choosen_word)):
#     letter = choosen_word[pos]
