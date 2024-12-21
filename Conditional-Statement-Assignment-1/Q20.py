"""Write a Python program that takes a month number (1–12) and outputs the corresponding season:
12, 1, 2: "Winter"
3, 4, 5: "Spring"
6, 7, 8: "Summer"
9, 10, 11: "Autumn" """

month=int(input('Enter a month number(1-12):'))
if month in [12,1,2]:
    print('Winter')
elif month in [3,4,5]:
    print('Spring')
elif month in [6,7,8]:
    print('Summer')
elif month in [9,10,11]:
    print('Autumn')
else:
    print('Please enetr a valid number')