"""Create a Python program that greets the user with the message "Welcome to the Haunted House". Then, ask the user whether they want to go "upstairs" or 
"downstairs". If they choose "downstairs", print "Game Over". If they choose "upstairs", ask if they want to "enter the room" or "stay outside". If they choose
"enter the room", print "Game Over". If they choose "stay outside", ask them to choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
"vampire", print "Game Over". If they choose "werewolf", print "You Win"."""

print('Welcome to the Haunted House!')
choice=input('Choose if you want to go upstairs or downstairs:')
if choice=='upstairs':
    action=input('Do you want to enter the room or stay outside?:')
    if action=='enter the room':
        print('Game Over')
    else:
        character=input('Choose between ghost, vampire, or werewolf:')
        if character=='ghost':
            print('Game Over')
        elif character=='vampire':
            print('Game Over')
        elif character=='werewolf':
            print('You Win')
        else:
            print('Invalid choice')
elif choice=='downstairs':
    print('Game Over')
else:
    print('Invalid choice.Game Over')