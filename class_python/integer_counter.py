print('This is an integer counter program.')
print('Press Enter to input the next number OR press Enter to finish.')

count = 0
total = 0

while True:
    line = input('input the integer here:')
    if line:
        try:
            number = int(line)
            print('integer',number,' entered')
            count += 1
            total += number
        except ValueError as err:
            print(err)
        trial += 1
        continue
    else:
        break
print('count =',count,'total =',total,'means =',count/total)
print('count=',count,'trial=',trial,'success=',count/trial)
    
