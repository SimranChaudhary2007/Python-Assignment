# Accept the age of 4 people and display the youngest one

Age1=int(input('Enter age of Person 1:'))
Age2=int(input('Enter age of Person 2:'))
Age3=int(input('Enter age of Person 3:'))
Age4=int(input('Enter age of Person 4:'))
if Age1<Age2 and Age1<Age3 and Age1<Age4:
    print('Person 1 is youngest')
elif Age2<Age1 and Age2<Age3 and Age2<Age4:
    print('Person 2 is youngest')
elif Age3<Age1 and Age3<Age2 and Age3<Age4:
    print('Person 3 is youngest')
else:
    print('Person 4 is youngest')

# OR

Age1=int(input('Enter age of Person 1:'))
Age2=int(input('Enter age of Person 2:'))
Age3=int(input('Enter age of Person 3:'))
Age4=int(input('Enter age of Person 4:'))
Age=min(Age1,Age2,Age3,Age4)
print(f'The youngest age is {Age}')