print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

direction = input("You're at a crossroad. Where do you want to go? Type left or right \n").lower()

if (direction == "left"):
    cross_road = input("You arrived at a lake. There is an island at the middle of the lake. \nType wait to 'wait' for a boat or Type 'swim' to swim across. \n").lower()

    if (cross_road == "wait"):
        door_choice = input("You arrived at the island unharmed. There is a house with three(3) doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()

        if (door_choice == 'red'):
            print("You entered a room full of beasts. Game over!")
        elif (door_choice == 'blue'):
            print("You entered a room full of dragons. Game over!")
        else:
            print("Yaaaayy! 🥳 You found the treasure. You won!")
else:
    print("You lost. Game over!")

