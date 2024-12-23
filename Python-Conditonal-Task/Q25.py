"""Accept the age, gender ('M', 'F'), and show type ('Matinee', 'Evening'):
Age < 12:
o Male or Female:
Matinee: Ticket = Rs500
Evening: Ticket = Rs700
Age >= 12 and < 60:
o Male:
Matinee: Ticket = Rs800
Evening: Ticket = Rs100
o Female:
Matinee: Ticket = Rs700
Evening: Ticket = Rs900
Age >= 60:
o Male or Female: Ticket = Rs600 """

age = int(input("Enter your age: "))
gender = input("Enter your gender (M or F): ")
show_type = input("Enter the show type (Matinee or Evening): ").lower()
if age < 12:
    if show_type == 'matinee':
        print("Ticket = Rs500")
    elif show_type == 'evening':
        print("Ticket = Rs700")
    else:
        print("Invalid show type")
elif 12 <= age < 60:
    if gender == 'M': 
        if show_type == 'matinee':
            print("Ticket = Rs800")
        elif show_type == 'evening':
            print("Ticket = Rs100")
        else:
            print("Invalid show type")
    elif gender == 'F':
        if show_type == 'matinee':
            print("Ticket = Rs700")
        elif show_type == 'evening':
            print("Ticket = Rs900")
        else:
            print("Invalid show type")
    else:
        print("Invalid gender input")
elif age >= 60:
    print("Ticket = Rs600")
else:
    print("Invalid age input")
