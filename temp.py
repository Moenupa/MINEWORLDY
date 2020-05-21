_list = [ [i, j, 17 - i - j] for i in range(1, 16) for j in range(1, 17 - i) ]
count = sum(i[-1] >= 9 for i in _list)
print(len(_list))#[=120]            # number of all situation is len(_list)
print(count)#[=28]                  # number of all x3>=9 situations is count

fib = (1/2)**n/root5*((1+root5)**n-(1-root5)**n)