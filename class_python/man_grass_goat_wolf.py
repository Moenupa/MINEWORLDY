pst = list('EEEE')
def chg(obj):
    if obj == 'E':
        obj = 'W'
    elif obj == 'W':
        obj = 'E'
    return obj
def chk2(obj1,obj2):
    if obj1 == obj2:
        return True
    else:
        return False
def chk3(obj1=pst[1],obj2=pst[2],obj3=pst[3]):
    if obj1 == obj2 and obj2 == obj3:
        return True
    else:
        return False
def chk4():
    if pst[0] == pst[1] and pst[1] == pst[2] and pst[2] == pst[3]:
        return True
    else:
        return False
while pst != list('WWWW'):
    if pst == list('EWEW'):
        pst = list('WWWW')
    elif chk2(pst[1]=pst[3]):
        if pst[1] == pst[2]:
            chg(pst[0])
            chg(pst[2])
print('Program complete!')
print(pst)
        
        
    
