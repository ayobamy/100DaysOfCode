# Control flow & logical operator

# movie age checkpoint
print("Welcome to the cinema 🎥")

age = int(input("How old are you?  "))

if age >= 18:
    print("You're old enough to see the movie")
    
    height = int(input("What is your height in cm?  "))
    if (height < 100):
        print("You can watch the movie at CINEMA 3")
    elif(height >= 100 and height < 120):
        print("You can watch the movie at CINEMA 2")
    else:
        print("You can watch the movie at CINEMA 1")
else:
    print("Sorry! You're not old enough to see the movie.")


