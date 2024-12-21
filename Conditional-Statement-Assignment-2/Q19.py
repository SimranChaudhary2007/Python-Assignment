# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

userinput=int(input('Enter a number:'))
if userinput%2==0 and userinput%3==0:
    print('Given number is divisible by both 2 and 3.')
elif userinput%2==0:
    print('Given number is divisible by 2.')
elif userinput%3==0:
    print('Given number is divisible by 3.')
else:
    print('The number is not divisible by both 2 and 3 ')