# Write a Python program to check if a given character is uppercase, lowercase, or a digit.

userinput=(input('enter a character:'))
if userinput.isupper():
    print('uppercase')
elif userinput.islower():
    print('lowercase')
elif userinput.isdigit():
    print('digit')
else:
    print('Invalid input')