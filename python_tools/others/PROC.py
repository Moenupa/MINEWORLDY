def procs0(a,b):
    '''
    Input: 2 int a, b
    Output: 2 int x, y
    '''
    sum = str(a+b).zfill(2)
    return int(sum[0]),int(sum[1])
def procs1(a,b,c):
    '''
    Input: a, b, c as 3 int
    Output: x, y as 2 int
    '''
    x1,y1 = procs0(a,b)
    x2,y = procs0(y1,c)
    z,x = procs0(x1,x2)
    return x,y
def procs2(a,b):
    '''
    Input: a, b as str
    Output: sum_ab as list
    '''
    len_max = max(len(a), len(b))
    if len_max == 1:
        x,y = procs0(a,b)
        sum_ab = str(x)+str(y)
    else:
    
    
        number_a = list(map(int, str(a).zfill(len_max)))
        number_b = list(map(int, str(b).zfill(len_max)))
        sum_ab = []
        for i in range(0, len_max, 2):
            
        for i in range(1, len_max, 2):
            
        sum_ab.reverse()
        len_sum = len(sum_ab)
    
    return sum_ab

def main():
    while True:
        func = input('procs0\\procs1\\procs2\\QUIT:').upper()
        if func == 'QUIT':
            break
        elif func == 'PROCS0' :
            a,b = input('a,b:').split(',')
            x,y = PROC0(int(a),int(b))
            print(str(x)+str(y))
            continue
        elif func == 'PROCS1':
            a,b,c = input('a,b,c:').split(',')
            x,y = PROC1(int(a),int(b),int(c))
            continue
        elif func == 'PROCS2':
            a,b = input('a,b:').split(',')
            print(''.join(str(i) for i in PROC2(a,b)))
            continue

main()
            


