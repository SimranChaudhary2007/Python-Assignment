"""N students take K apples and distribute them among each other evenly. The remaining (the indivisible) part remains in the basket. How many apples will
each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the
questions above."""

N=int(input('Enter number of students:'))
K=int(input('Enter number of apples:'))
student_gets=K//N
print(f'Each students gets:{student_gets} apple')
remaining=K%N
print(f'Remaining apple in basket:{remaining}')