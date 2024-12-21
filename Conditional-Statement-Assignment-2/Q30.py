"""Write a program to calculate the delivery cost based on the weight of the package:
If the package weighs less than 5kg, charge 5.
If it weighs between 5kg and 20kg, charge 10.
Check if the delivery is urgent; if yes, add $5 extra.
If it weighs more than 20kg, charge 20."""

weight=int(input('Enter the weight of package:'))
if weight<5:
    charge=5
    print(F'Cost of delivery={charge}')
elif 5<= weight <=20:
    charge=10
    print(F'Cost of delivery={charge}')
else:
    charge=20
    print(F'Cost of delivery={charge}')
delivery=input('Is the delivery urgent(yes/no):')
if delivery=='yes':
    total_charge=charge+5
    print(F'You have to pay an extra $5.So your total charge is {total_charge}')
else:
    print(F'No extra charge apply.Your total charge is {charge}')