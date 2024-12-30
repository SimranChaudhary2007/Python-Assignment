# Python program to count the space of a given string

string=input("Enter string:")
space_count=0
for i in string:
    if i.isspace():
        space_count+=1
print(f'Space count:{space_count}')