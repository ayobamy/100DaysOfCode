# checks if an number is odd or even

print("Welcome to the Odd or Even number checker!")

num = int(input("What number do you want to check 🔢 ? "))

if (num % 2 == 0):
    print("{:d} is an EVEN number!".format(num))
else:
    print("{:d} is an ODD number!".format(num))
