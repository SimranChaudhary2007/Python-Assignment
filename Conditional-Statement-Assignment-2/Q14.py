# Write a python program which accepts the radius of circle from user and compute the area.

import math
radius=int(input('Enter the raduis of circle:'))
if radius==0:
    print("Radius can't be 0")
elif radius<0:
    print("Radius can't be negative")
else:
    area= math.pi*radius*radius 
    print(f'Area of circle={area}')