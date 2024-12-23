"""Accept two numbers from the user:
If both numbers are even, print their sum.
If one is even and the other is odd, print their difference.
Otherwise, print their product."""

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1%2==0 and num2%2==0:
    print(num1+num2)
elif num1%2!=0 and num2%2!=0:
    print(num1*num2)
else:
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)