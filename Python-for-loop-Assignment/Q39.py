# Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.

sum_even=0
sum_odd=0
for i in range(1,101):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print(f'Sum of even numbers in the given range is {sum_even}')
print(f'Sum of odd numbers in the given range is {sum_odd}')