"""A company decided to give bonus to employee according to following criteria:
Time period of service    Bonus
More than 10 years         10%
>=6 and <=10                8%
Less than 6 years           5%  """

time_period=int(input('Enter your time period of service:'))
print(f'Time period:{time_period}years')
if time_period>10:
    print('Bonus:10%')
elif 6<= time_period <=10:
    print('Bonus:8%')
else:
    print('Bonus:5%')