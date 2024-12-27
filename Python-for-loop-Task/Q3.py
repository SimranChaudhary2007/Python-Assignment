# Write a python program to print a multiplication table of any number using for loop.

a=int(input('Enter a number:'))
for i in range(1,11,1):
    print(a,'*',i,'=',a*i)