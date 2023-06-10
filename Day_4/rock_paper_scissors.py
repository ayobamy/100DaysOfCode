# Rock, Paper and Scissors
# Rocks wins against Scissors (r > s)
# Scissors wins against Paper (s > p = 2 > 1)
# Paper wins against Rock (p > r = 1 > 0)
# Rock == 0, Paper == 1, Scissors == 2
import random

rock = '''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a
'''

paper = '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                 
'''

scissors = '''
                     88                                                       
                     ""                                                                                                               
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
'''

game_arts = [rock, paper, scissors]
# user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n"))

if (user_choice >= 3 or user_choice < 0):
    print("You entered an invalid number. You lost!")

else:
    print(f"You choose: \n{game_arts[user_choice]}\n")
    # computer choice
    cpu_choice = random.randint(0, 2)
    print(f"Computer choose: \n{game_arts[cpu_choice]}\n")

    if (cpu_choice == 2 and user_choice == 1):
        print("Scissors cuts paper. You lost!")
    elif (cpu_choice == 1 and user_choice == 0):
        print("Paper beats rock. You lost!")
    elif (cpu_choice == 0 and user_choice == 2):
        print("Rock smashes scissors. You lost!")
    elif (user_choice == 2 and cpu_choice == 1):
        print("Scissors cuts paper. You Won!")
    elif (user_choice == 1 and cpu_choice == 0):
        print("Paper beats rock. You Won!")
    elif (user_choice == 0 and cpu_choice == 2):
        print("Rock smashes scissors. You Won!")
    else:
        print("It's a draw!")
