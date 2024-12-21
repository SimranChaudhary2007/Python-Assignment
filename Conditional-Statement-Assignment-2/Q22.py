"""Write a program to accept percentage and display the category according to the following criteria:
Percentage        Category
<40                Failed
>=40 and <55        Fair
>=55 and <65        Good
>=65              Excellent """

percentage=int(input('Enter your percentage:'))
if percentage>=65:
    print('Excellent')
elif 55<= percentage <65:
    print('Good')
elif 40<= percentage <55:
    print('Fair')
else:
    print('Failed')