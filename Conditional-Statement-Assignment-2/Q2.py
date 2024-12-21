"""Create a Python program that starts by greeting the user with a message"Welcome to Treasure Land".
Then, prompt the user to choose a direction,either "left" or "right". If the user chooses "right", print "Game Over". If the user
chooses "left", ask whether they want to "swim" or "wait". If they choose"swim", print "Game Over". If they choose to "wait",
ask them to select a color:"red", "blue", or "yellow". If the user picks "blue" or "red", print "Game Over". If they select "yellow",
print "You Win"."""

print('Welcome to Treasure land.')
choice=input('Please enter direction:')
if choice=='right':
    print('Game Over')
elif choice=='left':
    action=(input('Enter if you want to swim or wait:'))
    if action=='swim':
        print('Game Over')
    else :
        action=='wait'
        color=input('Enter a colour(red, blue, or yellow):')
        if color=='red':
            print('Game Over')
        elif color=='blue':
            print('Game Over')
        elif color=='yellow':
            print('You Win')
        else:
            print('Invalid color')
else:
    print('Invalid input')