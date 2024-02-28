user = input()
password = input()

users = ("tim")
okie = ("abc123")

if (user.lower() in users.lower()) and (password in okie):
    print (f'Access Granted')
else:
    print (f'Incorrect Username/Password Combination')