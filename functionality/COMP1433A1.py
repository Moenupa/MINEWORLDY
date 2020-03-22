def cutleaf(loop_obj):
    if sum(loop_obj[:-1]) >= 10:
        del loop_obj[-1]
        return cutleaf(loop_obj)
    else:
        return loop_obj
def init():
    weight = [1,5,10]
    situs = [ [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10] for a1 in weight for a2 in weight for a3 in weight for a4 in weight for a5 in weight for a6 in weight for a7 in weight for a8 in weight for a9 in weight for a10 in weight]
    legalss = []
    for situ in situs:
        temp = cutleaf(situ)
        if temp not in legalss and temp != None:
            legalss.append(temp)
    return legalss
states = init()
record = [25600 for i in range(len(states))]
for i in range(len(states)):
    for weight in states[i]:
        if weight == 1:
            record[i] /= 2
        elif weight == 5:
            record[i] = record[i]*3/10
        elif weight == 10:
            record[i] /= 5


# record: frequancy*25600
# x: 1-10, y: 10-19

prop_Y = [sum(i) for i in states]
prop_X = [len(i) for i in states]
table = [ [ 0 for x in range(10)] for y in range(10) ]
print(len(states), len(prop_X), len(prop_Y))
for i in range(len(states)):
    #print("{0}: {1}: X{2}: Y{3}".format(states[i], record[i], x[i], y[i]))
    
    table[int(prop_Y[i]-10)][int(prop_X[i]-1)] += record[i]

EXY=0
EX=0
EY=0
for y in range(10):
    for x in range(10):
        EXY += (y+10)*(x+1)*(table[y][x])/25600
        EX += (x+1)*(table[y][x])/25600
        EY += (y+10)*(table[y][x])/25600
print(EXY-EX*EY)