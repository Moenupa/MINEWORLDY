def RPM(x, y):
    '''
    Russian Peasant Multiplication
    x, y: int
    return x * y
    '''
    A = []
    while y != 1:
        if y % 2 == 1:
            A.append(x)
            x += x
        y = int(y / 2)