# Ask a user for a username and password. If the username is correct, check if the password is correct, and display appropriate login messages.

correct_username='simran123'
correct_password='password123'
username=input('Enter your username:')
password=input('Enter your password:')
if username==correct_username:
    if password==correct_password:
        print('Login successfully.')
    else:
        print('Incorrect password. Please try again.')
else:
    print('Incorrect username. PLease try again.')