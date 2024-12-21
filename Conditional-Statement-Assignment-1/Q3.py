"""Write a program that asks the user for a number in the range of 1 to 12.
The program should display the corresponding month, 
where 1=january, 2=february, 3=march, 4=april, 5=may, 6=june, 7=july, 8=august, 9=september, 10=october, 11=november, 12=december.
The program should display an error message if the user enters a numberthat is outside the range of 1 to 12."""

month_number=int(input('enter a number:'))
if month_number==1:
    print('Janurary')
elif month_number==2:
    print('February')
elif month_number==3:
    print('March')
elif month_number==4:
    print('April')
elif month_number==5:
    print('May')
elif month_number==6:
    print('June')
elif month_number==7:
    print('July')
elif month_number==8:
    print('August')
elif month_number==9:
    print('September')
elif month_number==10:
    print('October')
elif month_number==11:
    print('November')
elif month_number==12:
    print('Decembr')
else:
    print('Please enter the number within the range 1 to 12')