# BMI(Body mass index) Calculator
# BMI = weight / height ** 2

weight = input("Enter your weight in metres(kg): ")
height = input("Enter your height in meters(m): ")

BMI = int(weight) / float(height) ** 2

print(int(BMI), end=" ")
print("kg/m^2")
