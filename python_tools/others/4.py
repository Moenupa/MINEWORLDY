a = input('a:')
b = input('b:')
k = len(a)
t = len(b)
len_max = max(k,t)
#get maximum digits
    
#fill a and b to the same length
a = str(a).zfill(len_max)
b = str(b).zfill(len_max)
#output a and b as str
    
#create list of a and b
number_a = list(map(int,list(a)))
number_b = list(map(int,list(b))
#output number a and b as list of ints
    
#add to sum
sumab = []
for i in range(0,len_max):
    sumab.append(a[len_max-i-1]+b[len_max-i-1])
sumab.reverse()
print(sumab)
    
#check if over 10
for i in range(0,len_max):
    if sumab[len_max-i-1] > 10:
        sumab[len_max-i-1] -= 10
        sumab[len_max-i-2] += 1
