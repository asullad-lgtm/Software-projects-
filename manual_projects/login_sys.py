users = {'admin': '1234',
         'akshay':'pass@1234'  
}

print("=======LOGIN SYSTEM========")

username = input('Enter Username: ')
password = input('Enter Password: ')

if username == "" or password =="":
    print('Field cannot be empty')
elif username in users and users[username]==password:
    print('Login Successfully....')
else:
    print('Login failed')