# Write a for loop which appends the type of each element in the first list to the second list.

first_lst=[123, "Hello", 1.15, True]
second_lst=[]
for i in first_lst:
    second_lst.append(type(i))
print(second_lst)