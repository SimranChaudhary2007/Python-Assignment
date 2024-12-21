"""Write a Python program that takes a color as input ("Red", "Yellow", "Green") 
and outputsthe corresponding action ("Stop", "Get Ready", "Go")."""

userinput=input('Enter a color:')
if userinput=='red':
    print('Stop')
elif userinput=='yellow':
    print('Get Ready')
elif userinput=='green':
    print('Go')
else:
    print('Inavlid input')