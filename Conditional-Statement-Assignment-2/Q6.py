"""WAP which accepts marks of four subjects and display total marks,percentage and grade.
Hint: more than 70 – distinction, more than 60 – first, more than 40 – pass, less than 40 – fail"""

subject1=int(input('Enter mark of Maths:'))
subject2=int(input('Enter mark of Science:'))
subject3=int(input('Enter mark of Computer:'))
subject4=int(input('Enter mark of English:'))
total_mark=subject1+subject2+subject3+subject4
print(f'Total_mark:{total_mark}')
percentange=total_mark/400*100
print(f'Percentange:{percentange}%')
if percentange>=70:
    print('Grade:distinction')
elif percentange>=60:
    print('Grade:first')
elif percentange>=40:
    print('pass')
else:
    print('Fail')