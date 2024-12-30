# Write a for loop that removes all vowels (a, e, i, o, u) from a string.

strings=input("Enter a string:")
vowels=("a","e","i","o","u")
for i in vowels:
    if i in strings:
        strings=strings.replace(i,'')
print(strings)