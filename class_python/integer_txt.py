
import os
os.chdir('C:\Drive_comp\python_work')
print(os.getcwd())
integers=[]
for i in open('integer.txt'):
    integers.append(i.strip('\n'))

print('Type integers, each followed by Enter;  or ^D or ^Z to finish.')

total=0
count=0

while True:
    try:
        if line:
            number=int(line)
            total+=number
            count+=1
    except ValueError as err:
            print(err)
            continue
    except EOFError:
            break
if count:
    print('count=',count,'total=',total,'mean=',total/count)
