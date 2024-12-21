"""Accept the age, gender ('M', 'F'), number of days and display the wages accordingly.
Age               Gender       Wage/day
>=18 and <30        M           700
                    F           750
>=30 and <=40       M           800
                    F           850 """

age=int(input('Enter age:'))
gender=input('Enter gender:')
if 18<= age <30 :
    if gender=='M':
        print('Wage/days:700')
    elif gender=='F':
        print('Wage/dyas:750')
    else:
        print('Invalid gender')
elif 30<= age <=40:
    if gender=='M':
        print('Wage/days:800')
    elif gender=='F':
        print('Wage/dyas:850')
    else:
        print('Invalid gender')
else:
    print('Age is outside the wage criteria.')