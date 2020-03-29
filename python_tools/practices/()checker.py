def checker(string):
    counter = 0
    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if i < 0:
            return False
    return True