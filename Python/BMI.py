height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height / 100) ** 2

print("Your BMI is", BMI)

if BMI <= 18.5:
    print("You are underweight. You need to eat more.")
elif BMI <= 24.9:
    print("You have a normal weight. Good job!")
elif BMI <= 29.9:
    print("You are overweight. Exercise more.")
elif BMI >= 30:
    print("You are obese. You need to lose some weight.")
else:
    print("You are too obese. Get some help from a professional.")