"""Begin with "Welcome to the Underwater World".
Ask the user to choose "dive deeper" or "surface".
If "dive deeper", ask them to "search for pearls" or "chase the fish".
If "search for pearls", print "You found a rare pearl. You Win!"
If "chase the fish", print "You got lost underwater. Game Over."
If "surface", print "You returned safely." """

print("Welcome to Underwater world!")
action=input("Choose if you want to 'dive depper' or 'surface':").lower()
if action=='dive deeper':
    choice=input("Do you want to 'search for pearls' or 'chase the fish':").lower()
    if choice=='search for pearls':
        print("You found a rare pearl. You Win!")
    elif choice=='chase the fish':
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice")
elif action=='surface':
    print("You returned safely.")
else:
    print("Invalid input. Game Over")