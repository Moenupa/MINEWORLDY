keys = []
for i in range(1,16,1):
    keys.append(str(i))
values = ['x + y','x - y','x * y','x / y','x  \\/-- y','x mod y','|x|','int(x)','eval(x)','float(x)','complex(x)','c.conjugate()','divmod(x,y)','pow(x,y)','x ** y']
d = dict(zip(keys,values))

for keys,values in d.items():
    print(keys,'. ',values)
func = input('Enter your preferance:')

def main(func):
    if func == '5':
        print('x // y')
    elif func == '6':
        print('x % y')
    elif func == '7':
        print('abs(x)')
    elif func in keys:
        print(d[func])
main(func)
