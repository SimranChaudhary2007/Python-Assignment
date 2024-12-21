"""A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest
possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can
get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total."""

class_a=int(input('Enter the number of students:'))
class_b=int(input('Enter the number of students:'))
class_c=int(input('Enter the number of students:'))
desk_required1=class_a//2 + class_a%2
print(f'Desk needed for class a:{desk_required1}')
desk_required2=class_b//2 + class_b%2
print(f'Desk needed for class b:{desk_required2}')
desk_required3=class_c//2 + class_c%2
print(f'Desk needed for class c:{desk_required3}')
print(f'Total desk needs to purchase:{desk_required1+desk_required2+desk_required3}')