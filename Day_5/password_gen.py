import random

print('''
Welcome to your custom PASSWORD GENERATOR! \n
8b,dPPYba,  ,adPPYYba, ,adPPYba, ,adPPYba,  ,adPPYb,d8  ,adPPYba, 8b,dPPYba,   
88P'    "8a ""     `Y8 I8[    "" I8[    "" a8"    `Y88 a8P_____88 88P'   `"8a  
88       d8 ,adPPPPP88  `"Y8ba,   `"Y8ba,  8b       88 8PP""""""" 88       88  
88b,   ,a8" 88,    ,88 aa    ]8I aa    ]8I "8a,   ,d88 "8b,   ,aa 88       88  
88`YbbdP"'  `"8bbdP"Y8 `"YbbdP"' `"YbbdP"'  `"YbbdP"Y8  `"Ybbd8"' 88       88  
88                                          aa,    ,88                         
88                                           "Y8bbdP" 
''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


num_letters = int(input("How many letters do you want to want?\n"))
num_symbols = int(input("\nHow many symbols do you want? \n"))
num_numbers = int(input("\nHow many numbers do you want? \n"))

passwrd = []

for letter in range(num_letters):
    passwrd.append(random.choice(letters))

for symbol in range(num_symbols):
    passwrd.append(random.choice(symbols))

for number in range(num_numbers):
    passwrd.append(random.choice(numbers))

random.shuffle(passwrd)

shuffled_passwrd = ""
for i in passwrd:
    shuffled_passwrd += i

print(f"\nHere is your unique password: {shuffled_passwrd}\n")
