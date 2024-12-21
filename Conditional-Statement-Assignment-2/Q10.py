"""Accept the grades from the user and display the grade according to the following criteria:
Below 25 --D
25 to 45 -- C
45 to 50 -- B
50 to 60 --B+
60 to 80 -- A
Above 80 -- A+"""

grade=int(input('Enter your grade:'))
if grade>80:
    print('A+')
elif grade>=60 and grade<=80:
    print('A')
elif grade>=50 and grade<60:
    print('B+')
elif grade>45 and grade<50:
    print('B')
elif grade>=25 and grade<45:
    print('C')
else:
    print('D')