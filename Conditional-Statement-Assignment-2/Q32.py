"""Create a program that suggests activities based on the weather:
If the weather is sunny, recommend outdoor activities like hiking or a picnic.
If the weather is rainy, check if the user has a raincoat or umbrella:
If yes, suggest going to a nearby mall or museum.
If no, recommend staying home and watching movies."""

weather=input("What's the weather outside?:")
if weather=='sunny':
    print("Since it's sunny you can do outdoor activities like hiking or a picnic.")
elif weather=='rainy':
    item=input('Do you have raincoat or umbrella?(yes/no):')
    if item=='yes':
        print('If you have it then you can go visit a nearby mall or museum.')
    else:
        print("It's better you stay home and watch movies.")
else:
    print('Invalid input')