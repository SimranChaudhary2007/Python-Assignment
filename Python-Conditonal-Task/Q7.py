"""Write a program that starts with a greeting: "Welcome to the Forest Adventure".
Prompt the user to choose a path: "left" or "right".
If "left", ask them to pick between "explore" or "rest".
If "explore", print "You found treasure!".
If "rest", print "You were attacked by wild animals. Game Over." """

print('Welcome to the Forest Adventure!')
path=input("Do you want to go 'left' or 'right':").lower()
if path=='left':
    choice=input("Pick between 'explore' or 'rest':").lower()
    if choice=='explore':
        print('You found treasure.')
    elif choice=='rest':
        print('You were attacked by wild animals. Game Over.')
    else:
        print('Invalid choice')
elif path=='right':
    print('Game Over')
else:
    print('Invalid input. Game Over')