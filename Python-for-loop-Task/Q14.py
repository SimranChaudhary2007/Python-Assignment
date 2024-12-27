# Accept string from the user and display only those characters which are present at an odd index.

string=input("Enter string:")
for i in range(len(string)):
    if i%2!=0:
        print(string[i])