# BMI calculator

weight = float(input("Enter your weight in kilogram(kg):  "))
height = float(input("Enter your height in metres(m): "))

bmi = weight / height ** 2
bmi = round(bmi)

if (bmi < 18.5):
    print("Your bmi is {:d}, you are underweight".format(bmi))
elif ((bmi > 18.5) and (bmi < 25)):
    print("Your bmi is {:d}, you have a normal weight".format(bmi))
elif ((bmi > 25) and (bmi < 30)):
    print("Your bmi is {:d}, you are overweight".format(bmi))
elif ((bmi > 30) and (bmi < 35)):
    print("Your bmi is {:d}, you are obese".format(bmi))  
else:
    print("Your bmi is {:d}, you are clinically obese".format(bmi))
