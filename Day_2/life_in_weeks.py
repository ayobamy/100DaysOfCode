# life in weeks challenge
# 1 year = 365 days = 52 weeks = 12 months
# assuming the person has 90 years to live

age = input("What is your age 🌍 ?  ")
# maximumhs age to live
age_max = 90
# age left to live
age_left = age_max - int(age)

# days left to live
days = age_left * 365

# weeks left to live
weeks = age_left * 52

# months left to live
months = age_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left to live")
