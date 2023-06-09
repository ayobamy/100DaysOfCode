# love calculator - shows the compatibility between two people

print("Welcome to the Love calculator! 💌")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

both_names = name1 + name2

# true word count
t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')

true_word = t + r + u + e

# love word count
l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')
e = both_names.count('e')

love_word =  l + o + v + e

love_score = str(true_word) + str(love_word)
love_score = int(love_score)

if (love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you got together like coke and mentos.")
elif (love_score > 40 and love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
