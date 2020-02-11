s = input('enter an integer:')
try:
    i = int(s)
    print('valid integer entered:',str(i))
except ValueError as err:
    print(err)
