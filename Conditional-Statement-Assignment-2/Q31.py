"""Write a program to check if a user qualifies for a loan:
If the user's income is above 50,000, check their credit score:
If the credit score is above 700, approve the loan.
If the credit score is between 600 and 700, approve with a higher interest rate.
If the credit score is below 600, reject the loan.
If the income is below 50,000, reject the loan."""

income=int(input('Enter your income:'))
if income>=50000:
    credit_score=int(input('Enter your credit score:'))
    if credit_score>700:
        print('Your loan is approved.')
    elif 600<= credit_score <=700:
        print('Your loan is approved with a higher interest rate.')
        print('Interest rate:10%')
    else:
        print('Your loan is rejected.')
else:
    print('Your loan is rejected.')