# Python program that accepts a string and calculate the number of digits and letters and space

string=input("Enter a string:")
digit_count=0
letter_count=0
space_count=0
for i in string:
    if i.isdigit():
        digit_count+=1
    elif i.isalpha():
        letter_count+=1
    else:
        space_count+=1
print(f'Letter={letter_count}')
print(f'Digit={digit_count}')
print(f'Space={space_count}')