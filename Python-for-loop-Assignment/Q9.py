# Given list is lst=[1,2,3,4] but print 1 and 4 only 

lst=[1,2,3,4]
for i in range(len(lst)):
    if i == 0 or i == len(lst)-1:
        print(lst[i])