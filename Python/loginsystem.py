d = {'admin':'admin'}
print('Welcome!')
print('Type "exit" anywhere to exit')

def goto(linenum):
    global line
    line = linenum
line = 0
def exit(name):
    if name == 'exit':
        global line
        line = 100
def quit(name,a=0):
    if name == 'quit':
        global line
        line = a
def chdir(Path='C:\Drive_comp\python_work'):
    import os
    os.chdir(Path)
        
#login
while True:
    if line == 0:
        choice = input('Type 1 to login, 2 to register:')
        exit(choice)
        if choice == '1':
            goto(1)
        elif choice == '2':
            goto(3)
        else:
            print('Please type 1 or 2')
    if line == 1:
        name = input('Input your login name:')
        exit(name)
        quit(name)
        if name in d:
            goto(2)
        else:
            print('login name do not exist.')
    elif line == 2:
        password = input('Input your login password:')
        exit(password)
        quit(password)
        if password == d[name]:
            print('login success')
            goto(5)
        else:
            print('password not correct, please try again.')
    elif line == 3:
        temp_name = input('Input your login name for register:')
        exit(temp_name)
        quit(temp_name)
        temp_password = input('Input your login password:')
        exit(temp_password)
        quit(temp_password)
        print('\tlogin name:'+temp_name+'\n\tlogin password:'+temp_password)
        goto(4)
    elif line == 4:
        confirmation = input('type 1 to confirm, 0 to retype.')
        exit(confirmation)
        if confirmation == '1':
            d[temp_name] = temp_password
            print('Register success, you can enter the system now.')
            goto(1)
        elif confirmation == '0':
            goto(3)
        else:
            print('enter a valid number.')
#magic do not touch
    elif line == 5:
        print('Welcome to the system.')
        goto(6)
    elif line == 6:
        function = input('Next?')
        exit(function)
        quit(function)
        if function == 'open':
            file = input('Filename:')
            quit(file)
            directory = input('Directory:')
            quit(directory)
            import os
            os.chdir(directory)
            exec(open(file.encode('UTF-8')).read())
        elif function == 'games':
            print('\t1.Love of Shape\n\t2.Magic Number Guess')
            game = input('Choose one game.')
            exit(game)
            quit(game)
            if game == '1':
                chdir()
                exec(open('Love.py').read())
            elif game == '2':
                chdir()
                exec(open('magic_number_guess.py').read())
#magic do not touch
    elif line == 100:
        break
print('Exiting System')
