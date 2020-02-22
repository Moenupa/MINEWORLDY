#this is a dec-bin trans tool

#looking for an input and check the number
while True:
    number = input('Enter a number in DEC:')
    try:
        int(number) > 0
        break
    except ValueError:
        print('Not a valid number.')
        continue

#magic do not touch
binary = []
number = int(number)
while True:
    vacant = number % 2
    vacant = int(vacant)
    number = int(number)
    binary.append(vacant)
    if number == 0:
        break
    else:
        if vacant == 1:
            number -= 1
            number = number/2
            continue
        elif vacant == 0:
            number = number/2
            continue
#

#
binary.reverse()
bin_number = '0'
for i in binary:
    i=str(i)
    bin_number = bin_number + i
bin_number = bin_number.lstrip('0')
print(bin_number)
#