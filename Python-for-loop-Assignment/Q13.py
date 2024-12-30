# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

lst=[1,2,3,"d",4,5,"a"]
integer=[]
string=[]
for i in lst:
    if isinstance(i,int):
        integer.append(i)
    else:
        string.append(i)
print(f'Integer:{integer}')
print(f'String:{string}')