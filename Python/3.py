#input ab int output xy int
def PROC0(a,b):
    number = a+b
    number = str(number).zfill(2)
    x = number[0]
    y = number[1]
    return int(x),int(y)

#input abc int output xy int
def PROC1(a,b,c):
    x1,y1 = PROC0(a,b)
    x2,y = PROC0(y1,c)
    z,x = PROC0(x1,x2)
    return x,y

#input ab as str output sum_ab as list
def PROC2(a,b):
    k = len(a)
    t = len(b)
    len_max = max(k,t)
    #get maximum digits
    a = str(a).zfill(len_max)
    b = str(b).zfill(len_max)
    #fill a and b to the same length
    number_a = list(a)
    number_b = list(b)
    number_a = [int(i) for i in number_a]
    number_b = [int(i) for i in number_b]
    #create list of a and b
    sum_ab = []
    for i in range(0,len_max):
        sum_ab.append(number_a[len_max-i-1]+number_b[len_max-i-1])
    sum_ab.reverse()
    len_sum = len(sum_ab)
    #add to sum
    for i in range(0,len_sum):
        if sum_ab[len_sum-i-1] > 10:
            sum_ab[len_sum-i-1] -= 10
            sum_ab[len_sum-i-2] += 1
        elif sum_ab[len_sum-i-1] == 10:
            sum_ab[len_sum-i-1] = 0
            sum_ab[len_sum-i-2] += 1
    #check if exceeds 10
    return sum_ab

def main():
    while True:
        func = input('PROC0\\PROC1\\PROC2\\QUIT:')
        if func == 'QUIT':
            break
        elif func == 'PROC0':
            a,b = input('a,b:').split(',')
            x,y = PROC0(int(a),int(b))
            print(str(x)+str(y))
            continue
        elif func == 'PROC1':
            a,b,c = input('a,b,c:').split(',')
            x,y = PROC1(int(a),int(b),int(c))
            continue
        elif func == 'PROC2':
            a,b = input('a,b:').split(',')
            print(''.join(str(i) for i in PROC2(a,b)))
            continue

main()
            


