#  Write a program to print the factorial of a number accepted from user.

num=int(input("Enter a number:"))
result=1
for i in range(1,num+1):
    result*=i
print(f'Factorial of {num} is {result}')