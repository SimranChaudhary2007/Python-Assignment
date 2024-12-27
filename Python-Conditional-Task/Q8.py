"""Write a program starting with "Welcome to the Jungle Survival Challenge".
Ask the user to "search for food" or "build a shelter".
If "search for food", ask to choose between "hunt" or "gather".
If "hunt", print "You were attacked by a wild animal. Game Over."
If "gather", print "You found enough food. You Win!"
If "build a shelter", print "Your shelter collapsed in the rain. Game Over." """

print('Welcome to the Jungle Survival challenge!')
action=input("Now choose if you want to either 'search for food' or 'build a shelter':").lower()
if action=='search for food':
    choice=input("Do you want to 'hunt' the food or 'gather' it?:").lower()
    if choice=='hunt':
        print('You were attacked by a wild animal. Game Over.')
    elif choice=='gather':
        print('You found enough food. You Win!')
    else:
        print('Invalid choice')
elif action=='build a shelter':
    print('Your shelter collapsed in the rain. Game Over.')
else:
    print('Invalid input. Game Over')