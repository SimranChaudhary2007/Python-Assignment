# Write a program to input three numbers and find the largest among them using nested if-else.

num1=int(input('Enter 1st number:'))
num2=int(input('Enter 2nd number:'))
num3=int(input('Enter 3rd number:'))
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print(F'The largest number is:{largest}')