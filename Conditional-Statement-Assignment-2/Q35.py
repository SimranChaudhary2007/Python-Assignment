"""Create a Python program that greets the user with the message "Welcome to the Magic Forest". Then, ask the user whether they want to go "north" or
"south". If they choose "south", print "Game Over". If they choose "north", ask if they want to "cross the river" or "follow the path". If they choose "cross the
river", print "Game Over". If they choose "follow the path", ask them to choose between "fairy", "ogre", or "elf". If they choose "ogre" or "fairy",
print "Game Over". If they choose "elf", print "You Win"."""

print('Welcome to the magic Forest!')
choice=input('Choose if you want to go to north or south:')
if choice=='north':
    action=input('Do you want to cross the river or follow the path:')
    if action=='cross the river':
        print('Game over')
    else:
        character=input('Choose between fairy, ogre, or elf:')
        if character=='fairy':
            print('Game Over')
        elif character=='ogre':
            print('Game Over')
        elif character=='elf':
            print('You Win')
        else:
            print('Invalid choice')
elif choice=='south':
    print('Game Over')
else:
    print('Invalid input. Game Over')