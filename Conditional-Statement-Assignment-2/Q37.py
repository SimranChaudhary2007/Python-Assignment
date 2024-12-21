"""Create a Python program that greets the user with the message "Welcome to the Pirate Island". Then, ask the user whether they want to go "left" or "right".
If they choose "right", print "Game Over". If they choose "left", ask if they want to "dig for treasure" or "sail the ship". If they choose "dig for treasure", print
"Game Over". If they choose "sail the ship", ask them to choose between "shark", "pirate ship", or "mermaid". If they choose "shark" or "pirate ship",
print "Game Over". If they choose "mermaid", print "You Win"."""

print('Welcome to the Pirate Island!')
choice=input('Choose if you want to go left or right:')
if choice=='left':
    action=input('Do you want to dig for treasure or sail the ship?:')
    if action=='dig for treasure':
        print('Game Over')
    else:
        character=input('Choose between shark, pirate ship, or mermaid:')
        if character=='shark':
            print('Game Over')
        elif character=='pirate ship':
            print('Game Over')
        elif character=='mermaid':
            print('You Win')
        else:
            print('Invalid choice')
elif choice=='right':
    print('Game Over')
else:
    print('Invalid choice. Game Over')