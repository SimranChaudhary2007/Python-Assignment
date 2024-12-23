"""Accept age, gender ('M', 'F'), and income and calculate the tax:
Age >= 18 and < 60:
Male:
Income > 10,00,000: Tax = 30%
Income between 5,00,000 and 10,00,000: Tax = 20%
Income <= 5,00,000: Tax = 10%
Female:
Income > 10,00,000: Tax = 25%
Income between 5,00,000 and 10,00,000: Tax = 15%
Income <= 5,00,000: Tax = 5%
Age >= 60:
Male or Female:
Income > 10,00,000: Tax = 20%
Income <= 10,00,000: Tax = 10%"""

age=int(input("Enter your age:"))
gender=input("Enter your gender(M or F):").lower()
income=int(input("Enter your salary:"))
if 18<= age <60:
    if gender=='M':
        if income>1000000:
            print('Tax=30%')
            final_income=income*(1+30/100)
            print(f'Final income:{final_income}')
        elif 500000< income <=1000000:
            print('Tax=20%')
            final_income=income*(1+20/100)
            print(f'Final income:{final_income}')
        else:
            print('Tax=10%')
            final_income=income*(1+10/100)
            print(f'Final income:{final_income}')
    else:
        if income>1000000:
            print('Tax=25%') 
            final_income=income*(1+25/100)
            print(f'Final income:{final_income}')
        elif 500000< income <=1000000:
            print('Tax=15%')
            final_income=income*(1+15/100)
            print(f'Final income:{final_income}')
        else:
            print('Tax=5%')
            final_income=income*(1+5/100)
            print(f'Final income:{final_income}')
elif age >= 60:
    if gender=='M' or gender=='F':
        if income>1000000:
            print('Tax=20%')
            final_income=income*(1+20/100)
            print(f'Final income:{final_income}')
        else:
            print('Tax=20%')
            final_income=income*(1+20/100)
            print(f'Final income:{final_income}')   
else:
    print("Invalid input")