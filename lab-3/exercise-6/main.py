user = input()
pw = input()

users = ("tim")
password = ("abc123")

if (user.lower() in users.lower()) and (pw in password):
    print (f'Access Granted')
elif (user.lower() not in users.lower()) and (pw in password):
    print (f'Incorrect Username')
elif (user.lower() in users.lower()) and (pw not in password):
    print (f'Incorrect Password')
else:
    print (f'Incorrect Username and Password')