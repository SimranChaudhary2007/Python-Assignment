"""Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
Pizza: $10
Burger: $7
Pasta: $8"""

food=input('Enter the menu item:')
if food=='Pizza':
    print('$10')
elif food=='Burger':
    print('$7')
elif food=='Pasta':
    print('$8')
else:
    print('Invalid option')