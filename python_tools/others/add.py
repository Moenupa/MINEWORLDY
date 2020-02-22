#this is a program to solve addition in 3 digits

#introduction to the subject
print(' -------------------------------------------------- \n'
      '| Enter your number for addition, 3 digits or less.|\n'
      '| Enter 0 to finish.                               |\n'
      '| You have a maxium of 10 number input.            |\n'
      ' -------------------------------------------------- \n')
#introduction to the subject

#reading number
temp = []
count = 0
while True:
    number = input('Enter your number for addition:')
    if number == '0':
        break
    elif count == 9:
        try:
            trial = int(number)
            if trial > 999:
                print('The number execeeds 999.')
                continue
            else:
                temp.append(number.zfill(3))
                count += 1
                break
        except ValueError:
            print('Please enter a number.')
            continue
    else:
        try:
            trial = int(number)
            if trial > 999:
                print('The number exceeds 999.')
                continue
            else:
                temp.append(number.zfill(3))
                count += 1
                continue
        except ValueError:
            print('Please enter a number.')
            continue
#reading number

#extract number by digit
extract3 = []
extract2 = []
extract1 = []
def extraction(name,position):
    for x in temp:
        name.append(int(x[position]))
extraction(extract3,-1)
extraction(extract2,-2)
extraction(extract1,-3)
#extract number by digit

#add digits together
sum3 = 0
sum2 = 0
sum1 = 0
sum0 = 0
def add(name):
    tempsum = 0
    for i in name:
        tempsum += i
    return tempsum
sum3 = add(extract3)
sum2 = add(extract2)
sum1 = add(extract1)
#add digits together

#check if one digit exceeds 10
def check(name1,name2):
    while True:
        if name1 <10:
            break
        else:
            name2 += 1
            name1 -= 10
            continue
    return name1,name2
sum3,sum2 = check(sum3,sum2)
sum2,sum1 = check(sum2,sum1)
sum1,sum0 = check(sum1,sum0)
#check if one digit exceeds 10

#delete 0s at the front
#and print out the total sum
sums = str(sum0)+str(sum1)+str(sum2)+str(sum3)
print(sums.lstrip('0'))
#delete 0s at the front
#and print out the total sum


