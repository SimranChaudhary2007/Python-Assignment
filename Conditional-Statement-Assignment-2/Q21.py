"""Accept the following from the user and calculate the percentage of class attended:
a. Total number of days
b. Total number of days for absent
After calculating percentage show that, if the percentage is less than 75,than student will not be able to sit in exam."""

working_days=int(input('Enter the total number of working days:'))
absent_days=int(input('Enter the total numbeer of absent days:'))
days_present=working_days-absent_days
print(f'Class attended:{days_present}')
present_percentage=(days_present/working_days)*100
print(f'Percentage of class attended:{present_percentage}%')
if present_percentage<75:
    print('Student will not be able to sit in exam')
else:
    print('Student will be able to sit in exam.')