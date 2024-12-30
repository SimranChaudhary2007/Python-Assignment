# Python program to calculate the sum of all the odd numbers within the given range.

start=int(input("Enter the start of range:"))
end=int(input("Enter the end of range:"))
sum=0
for i in range(start,end+1):
    if i%2!=0:
        sum=sum+i
        print(i)
print(f'The sum of all the odd numbers within the range is {sum}') 