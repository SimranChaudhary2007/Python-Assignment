# given list is [1,2,3,4] but expected output is [1,8,27,64]

lst=[1,2,3,4]
new_lst=[]
for i in lst:
     new_lst.append(i**3)
print(new_lst)