"""Write a Python program to check car loan eligibility:
Salary >= 50,000 and Credit Score >= 700: "Eligible"
Otherwise: "Not Eligible" """

Salary=int(input('Enter your salary:'))
Credit_score=int(input("Enter your credit score:"))
if Salary>=50000 and Credit_score>=700:
    print('Eligible')
else:
    print('Not Eligible')