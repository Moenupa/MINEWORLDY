#this is a program to solve addition

print('Enter your number:')

#introduction to the subject



def PROC0(a,b):
    sum = int(a) +int(b)
    sum.zfill(2)
    sum = str(sum)
    x = int(sum[0])
    y = sum[1]

#PROC2()
#PROC1()
#PROC0()

numbers = []
while True:
    number = input('number:')
    if number == 'q':
        break
    else:
        numbers.append(number)
lenses = []
for number in numbers:
    lens = len(number)
    lenses.append(lens)
    