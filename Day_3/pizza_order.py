print("Welcome to Python Pizza Deliveries! 🍕")

size = input("What size of pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni 🌶️ ? Y or N?  ")
add_cheese = input("Do you want extra cheese 🧀 ? Y or N? ")

amt = 0

if (size == "S"):
    amt = 15
    if (add_pepperoni == "Y"):
        amt += 2
    if (add_cheese == "Y"):
        amt += 1

elif (size == "M"):
    amt = 20
    if (add_pepperoni == "Y"):
        amt += 3
    if (add_cheese == "Y"):
        amt += 1

elif (size == "L"):
    amt = 25
    if (add_pepperoni == "Y"):
        amt += 3
    if (add_cheese == "Y"):
        amt += 1

print("Your final bill is: ${:d}".format(amt))
