"""Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give them options. If vegetarian, ask if they want "Salad" or "Pasta". 
If non-vegetarian, ask if they want "Chicken" or "Fish" """

choice=input('Do you want vegeterian or non vegetarian?:').lower()
if choice=='vegeterian':
    food=input('Do you like to have Salad or Pasta:').lower()
    print('Thanks for the order!')
elif choice=='non vegeterian':
    food=input('Do you like to have Chicken or Fish:').lower()
    print('Thanks for the order!')
else:
    print("Sorry we don't have that option.")