"""Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
Cost price(in Rs)       Tax
>100000                 15%
>50000 and <=100000     10%
<=50000                 5%  """

cost_price=int(input('Enter the cost price of bike:Rs'))
if cost_price>100000:
    print('Tax to be paid=15%')
elif cost_price>50000 and cost_price<=100000:
    print('Tax to be paid=10%')
else:
    print('Tax to be paid=5%')