"""Create a Python program that greets the user with the message "Welcome to the Jungle Adventure". Then, ask the user whether they want to go "left" or
"right". If they choose "right", print "Game Over". If they choose "left", ask if they want to "climb a tree" or "explore the cave". If they choose "climb a tree",
print "Game Over". If they choose "explore the cave", ask them to choose between "bear", "tiger", or "snake". If they choose "bear" or "tiger", print
"Game Over". If they choose "snake", print "You Win"."""

print('Welcome to the Jungle Adventure!')
choice=input('Choose if you want to go left or right:')
if choice=='left':
    action=input('Do you want to climb a tree or explore the cave?:')
    if action=='climb a tree':
        print('Game Over')
    else:
        animal=input('Choose between bear, tiger, or snake:')
        if animal=='bear':
            print('Game Over')
        elif animal=='tiger':
            print('Game Over')
        elif animal=='snake':
            print('You Win')
        else:
            print('Invalid choice')
elif choice=='right':
    print('Game Over')
else:
    print('Invalid choice. Game Over')