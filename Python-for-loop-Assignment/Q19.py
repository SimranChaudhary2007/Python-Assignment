#  Print multiplication table of  1,2,3,4,5,6,7,8 

for number in range(1,9):
    print(f'Multipication of {number}')
    for i in range(1,11):
        print(number,"*",i,"=",number*i)