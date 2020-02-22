def floor(number):
    global number
    if number >= 1:
        number -= 1
def dec_to_bin(f,n):
    loop_time = int(n)
    #processing n
    bin_list = []
    f = eval(f)
    while True:
        if loop_time  == 0:
            print('0.'+''.join(str(i) for i in bin_list))
            break
        else:
            f = f*2
            loop_time -= 1
            if f >= 1:
                bin_list.append(1)
                f -= 1
            else:
                bin_list.append(0)
            continue

f=input('f:')
n=input('n:')
dec_to_bin(f,n)

    
