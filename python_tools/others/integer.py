s = input('enter an integer:')
try:
    i = int(s)
        if (i % 2 == 1):
            print(i,'is odd.')
        else:
            print(i,'is even.')
except ValueError as err:
    print(err)
