magic_number = 111
while True:
    guess = int(input('Enter your guess here:'))
    if guess != magic_number:
        print('Incorrect. Try again.')
        continue
    else:
        print('Spot on!')
        break
