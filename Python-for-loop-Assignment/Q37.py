# Python program to count the number of even and odd numbers from a series of numbers.  

series=[10,15,20,25,30,35,40]
even_count=0
odd_count=0
for i in series:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f'Number of even in the series is {even_count}')
print(f'Number of odd in the series is {odd_count}')