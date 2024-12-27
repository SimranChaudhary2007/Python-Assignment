"""Accept the age, gender ('M', 'F'), and membership type ('Monthly', 'Yearly'):
Age >= 18 and < 30:
o Male:
Monthly: Rs50
Yearly: Rs500
o Female:
Monthly: Rs45
Yearly: Rs450
Age >= 30 and <= 50:
o Male or Female:
Monthly: Rs60
Yearly: Rs600
Age > 50:
o Male or Female:
Monthly: Rs40
Yearly: Rs400 """

age = int(input("Enter your age: "))
gender = input("Enter your gender (M or F): ")
membership_type = input("Enter membership type (Monthly or Yearly): ").lower()

if 18 <= age < 30:
    if gender == 'M':  
        if membership_type == 'monthly':
            print("Fee = Rs50")
        elif membership_type == 'yearly':
            print("Fee = Rs500")
        else:
            print("Invalid membership type")
    elif gender == 'F': 
        if membership_type == 'monthly':
            print("Fee = Rs45")
        elif membership_type == 'yearly':
            print("Fee = Rs450")
        else:
            print("Invalid membership type")
    else:
        print("Invalid gender input")
elif 30 <= age <= 50:
    if membership_type == 'monthly':
        print("Fee = Rs60")
    elif membership_type == 'yearly':
        print("Fee = Rs600")
    else:
        print("Invalid membership type")
elif age > 50:
    if membership_type == 'monthly':
        print("Fee = Rs40")
    elif membership_type == 'yearly':
        print("Fee = Rs400")
    else:
        print("Invalid membership type")
else:
    print("Invalid age input")
