# Take two numbers and find the greater of the two. If they are equal, check if the number is positive, negative, or zero.

num1=int(input('Enter 1st number:'))
num2=int(input('Enter 2nd number:'))
if num1>num2:
    print(F'Greater number is {num1}')
elif num1<num2:
    print(F'Greater number is {num2}')
else: 
    if num1>0:
        print('Positive')
    elif num1<0:
        print('Negative')
    else:
        print('Zero')