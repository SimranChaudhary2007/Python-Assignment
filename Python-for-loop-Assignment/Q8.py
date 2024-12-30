#  given list is [1,2,3,4] but expected output in new list [2,3,4,5]

lst=[1,2,3,4]
new_lst= []
for i in lst:
    new_lst.append(i+1)
print(new_lst)