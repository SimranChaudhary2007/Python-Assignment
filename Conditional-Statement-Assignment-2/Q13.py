"""A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for their 
salary and year of service and print the net bonus amount."""

salary=int(input('Enter your salary:'))
service_year=int(input('Enter your service year:'))
print(f'Salary:Rs {salary}')
print(f'Service year:{service_year} years')
if service_year>5:
    bonus=salary*5/100
    print('Bonus:5%')
    print(f'Net bonus amount:Rs {bonus}')
else:
    print('No bonus')