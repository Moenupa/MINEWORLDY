print('Type integers, each followed by Enter; or ^D ro ^Z to finish')

total=0
count=0

while True:
    try:
        line=input()
        if line:
            number=int(line)
            total+=number
            count+=1
        except ValueError as err:
            print(err)
            continue
        except E0FError:
            break
if count:
    print('count=',count,'total=',total,'mean=',total/count)
