"""Accept a BMI value from the user:
If BMI < 18.5, print "Underweight".
If 18.5 ≤ BMI < 24.9, print "Normal weight".
If 25 ≤ BMI < 29.9, print "Overweight".
If BMI ≥ 30, print "Obesity"."""

BMI_value=float(input("Enter you BMI value:"))
if BMI_value<18.5:
    print("Underweight")
elif 18.5 <= BMI_value < 24.9:
    print("Normal weight")
elif 25 <= BMI_value < 29.9:
    print("Overweight")
else:
    print("Obesity")