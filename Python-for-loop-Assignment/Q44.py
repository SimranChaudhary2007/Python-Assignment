"""You have two lists of numbers, and you need to find out which numbers appear in both lists.
Given two lists of numbers [1,2,3,4,5] and [3,4,5,6,7] write a for  loop to find the common elements"""

lst1=[1,2,3,4,5]
lst2=[3,4,5,6,5]
for i in lst1:
    if i in lst2:
        print(i)