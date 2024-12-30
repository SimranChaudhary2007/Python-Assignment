# Python program to calculate the sum of all the even numbers within the given range.

start=int(input("Enter the start of range:"))
end=int(input("Enter the end of range:"))
sum=0
for i in range(start,end+1):
    if i%2==0:
        sum=sum+i
print(f'The sum of all the even numbers within the given range is {sum}')