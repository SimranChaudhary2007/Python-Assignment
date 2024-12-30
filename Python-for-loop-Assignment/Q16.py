# Python program to check the validity of username and password input by users

for i in range(3,0,-1):
    user_name=input("Enter valid user name:")
    password=input("Enter valid password:")
    if user_name!="simran" or password!="1234":
       if i==1:
           continue
       print("Invalid username or password.","Please try again.",i-1,"attempt left")
    else:
        print("logged in successfully")
        break
else:
    print("You are blocked")