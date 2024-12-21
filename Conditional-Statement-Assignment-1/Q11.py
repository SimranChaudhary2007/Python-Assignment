"""Write a Python program to categorize a person’s age:
Age < 13: Child
13 <= Age <= 19: Teenager
Age > 19: Adult"""

age=int(input('enter age:'))
if age<13:
    print('child')
elif age>=13 and age<=19:
    print('teenager')
else:
    print('adult')