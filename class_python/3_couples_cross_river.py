def genAllStatus():
    '''
    Output all status
    0 represent the boat
    12,34,56 represents the three couples
    '''
    s = 'EW'
    list_all = list(a+b+c+d+e+f+g for a in s for b in s for c in s for d in s for e in s for f in s for g in s)
    return list_all
def isLegal(status):
    '''
    Input: status
    Output: True or False check if legal
    '''
    if (status[0]!=status[1] and status[1]==status[2]==status[3]==status[4]==status[5]==status[6])\
        or (i[2]!=i[1] and (i[2]==i[3] or i[2]==i[5]))\
        or (i[4]!=i[3] and (i[4]==i[1] or i[4]==i[5]))\
        or (i[6]!=i[5] and (i[6]==i[1] or i[6]==i[3])):
        return False
    else:
        return True
def isNeighbor(status1,status2):
    '''
    Input: status1 and status2 as two status
    Output: True or False check if Neighbor
    '''
    difference = 0
    if status1[0] != status2[0]:
        for i in range(1,7):
            if status1[i] != status2[i]:
                difference += 1
        if difference ==1 or difference == 2:
            return True
        else:
            return False
    else:
        return False
def linkStatus(lst):
    '''
    Input: lst as a list containing legal status
    Output: dictionary that links the legal status with others
    '''
    d = {}
    for i in lst[:]:
        temp = []
        for x in lst[:]:
            if isNeighbor(i,x) == True:
                temp.append(x)
        d[i] = temp
    return d
def printPath(status1,status2):
    '''
    Input: status1 and status2 as two legal status
    Output: print the transition text of couples 1-2
    '''
    index = ''
    for i in range(7):
        if status1[i] == status2[i]:
            index += str(i)
    index1,index2 = int(index[0]),int(index[1])
    person1,person2 = getId(index1),getId(index2)
    print(person1.title(),'from',status1[index1],'go to',status1[index2],'side')
    print(person2.title(),'from',status2[index1],'go to',status2[index2],'side')

def getId(num):
    if num == 1:
        return 'woman 1'
    elif num == 2:
        return 'men 1'
    elif num == 3:
        return 'woman 2'
    elif num == 4:
        return 'men 2'
    elif num == 5:
        return 'woman 3'
    elif num == 6:
        return 'men 3'

def main(start='EEEEEEE',end='WWWWWWW'):
    list_all = genStatus()
    list_legal = []
    for i in list_all:
        if isLegal(i) == True:
            list_legal.append(i)

    #list_legal represent all legal status
    
