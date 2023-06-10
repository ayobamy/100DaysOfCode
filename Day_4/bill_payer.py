# a program that randomly selects who buys the meal in a restaurant
import random

name_string = input("Give me everybody's name, seperated by a comma.  ")\
# split the names
names = name_string.split(", ")

choice = random.randint(0, len(names) - 1)

payer = names[choice]

print(f"{payer} is going to buy the meal today!")
