'''
A quiz about probability
number of cases are big
so solve in python codes instead
below is the question (Q1)
'''

'''
Question 1: Coins in a Bag. There are 10 coins in a bag, where 5 of them are one-dollar
coins, 3 five-dollar coins, and 2 ten-dollar coins. We assume that each coin has equal chances
to be taken out of the bag. (Total: 45’)
(a) We randomly take out two coins c1 and c2 (at once) from the bag, please describe the
sample space S reflecting the value sum of c1 and c2. (5’)
(b) We take out the two coins sequentially without putting back, first c1 then c2. What is the
probability that the value of c1 is larger than c2. (5’)
(c) We sequentially take out a coin, record the value, and put it back. We will stop till the
value sum of the coins taken out is ≥ 10 dollars. Let X denote number of coins taken out till
stop. What is P(X ≤ 3)? (10’)
(d) To continue the story in (c), let Y denotes the value sum of the coins taken out till stop.
Are X and Y independent? Why? (5’)
(e) We have defined X and Y in (c) and (d). What is the expected value and standard
deviation of Y , i.e., E[Y ] and σ(Y ). (10’)
(f) To continue with (e), how about the covariance of X and Y , i.e., Cov(X, Y )? (10’)

'''

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