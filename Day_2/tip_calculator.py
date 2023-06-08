# tip calculator

print("Welcome to the tip calculator.💰")

# ask for the total bill amount
bill_amt = input("What was the total bill 💸 ? $")
# ask for the percentage tip
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15?  ")
# ask for the number of persons spliting the bill
num_persons = input("How many persons to split the bill?  ")

# convert the type to float from the string input
bill_amt = float(bill_amt)

# calculate the total bill including the tip
total_bill = bill_amt + (int(tip_percent) * 0.01 * bill_amt)

# get the amount each person would pay
bill_per_person = round(total_bill / int(num_persons), 2)

print("Each person should pay ${:.2f}".format(bill_per_person))
