"""Write a program to determine if a candidate is eligible for a job:
If the candidate's age is >= 18, check if they have a degree.
If they have a degree, check their work experience:
More than 3 years: Display "Highly Eligible."
1-3 years: Display "Eligible."
Less than 1 year: Display "Under Review."
If the candidate's age is below 18, display "Not Eligible." """

age=int(input('Enter your age:'))
if age>=18:
    degree=input('Do you have degree(yes/no)?:')
    if degree=='yes':
        work_experience=int(input('Enter you work experience:'))
        if work_experience>3:
            print('Highly Eligible')
        elif 1<= work_experience <=3:
            print('Eligible')
        else:
            print('Under review')
    else:
        print('Sorry degree is must.')
else:
    print('Not Eligible')