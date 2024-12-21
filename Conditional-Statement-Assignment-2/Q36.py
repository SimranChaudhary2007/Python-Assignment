"""Create a Python program that greets the user with the message "Welcome to the Space Mission". Then, ask the user whether they want to go "to the moon"
or "to Mars". If they choose "to Mars", print "Game Over". If they choose "to the moon", ask if they want to "land on the surface" or "stay in orbit". If they
choose "land on the surface", print "Game Over". If they choose "stay in orbit", ask them to choose between "alien", "asteroid", or "satellite". If they choose
"alien" or "asteroid", print "Game Over". If they choose "satellite", print "You Win"."""

print('Welcome to the Space Mission!')
choice=input('Choose if you want to go to the moon or to Mars:')
if choice=='to the moon':
    action=input('Do you want to land on the surface or stay in orbit:')
    if action=='land on the surface':
        print('Game over')
    else:
        character=input('Choose between alien, asteroid, or satellite:')
        if character=='alien':
            print('Game Over')
        elif character=='asteroid':
            print('Game Over')
        elif character=='satellite':
            print('You Win')
        else:
            print('Invalid choice')
elif choice=='to Mars':
    print('Game Over')
else:
    print('Invalid input. Game Over')
