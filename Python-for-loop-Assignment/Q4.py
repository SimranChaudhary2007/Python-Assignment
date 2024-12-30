# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

lst=[1,"a","c",2,3,4]
for i in lst:
    if isinstance(i,int):
        print(i)