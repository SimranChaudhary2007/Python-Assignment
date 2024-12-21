"""Write a Python program to check login credentials:
Username: "admin", Password: "password123"
If correct, print "Access Granted"; otherwise, print "Access Denied." """

username=input('Enter your username:')
password=input('Enter your password:')
if username=='admin' and password=='password123':
    print('Access Granted')
else:
    print('Access Denied')