# checks if a year is a leap year

print("Welcome to the leap year checker! 🌐")

year =  int(input("Enter the year you want to check:  "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("{:d} is a leap year".format(year))
        else:
            print("{:d} is NOT a leap year".format(year))
    else:
        print("{:d} is a leap year".format(year))
else:
    print("{:d} is NOT a leap year".format(year))
