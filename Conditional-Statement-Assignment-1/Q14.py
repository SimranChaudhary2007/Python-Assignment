"""Write a Python program to check eligibility for a job based on age and experience:
Age > 18 and Experience >= 2 years: Eligible
Otherwise: Not Eligible"""

age=int(input("Enter your age:"))
experience=int(input('enter your experience:'))
if age>18 and experience>=2:
    print('Eligible')
else:
    print('Not eligible')