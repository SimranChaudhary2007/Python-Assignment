"""Start with "Welcome to the Haunted Castle".
Ask the user to choose "enter the castle" or "run away".
If "enter the castle", ask them to choose a door: "red", "green", or "black".
If "red", print "You entered a room full of flames. Game Over."
If "green", print "You found the treasure. You Win!"
If "black", print "You were captured by ghosts. Game Over."
If "run away", print "You escaped safely." """

print('Welcome to the Haunted Castle!')
action=input("Now choose if you want to either 'enter the castle' or 'run away':").lower()
if action=='enter the castle':
    color=input("Choose a door between 'red', 'green', or 'black':").lower()
    if color=='red':
        print('You entered a room full of flames. Game Over.')
    elif color=='green':
        print('You found the treasure. You Win!')
    elif color=='black':
        print('You were captured by ghosts. Game Over.')
    else:
        print('Invalid choice')
elif action=='run away':
    print('You escaped safely.')
else:
    print("Invalid input. Game Over")