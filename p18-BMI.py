
weight = float(input("Please enter your weight in Kgs: "))
h = float(input("Please enter your height in meters: "))

height = h * h
bmi = weight / height

if bmi < 19:
    print("You are underweight")
elif 19 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
