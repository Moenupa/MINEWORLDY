magic_number = 397
down_range = magic_number - 100
up_range = magic_number + 100
print('Welcome to the guessing game!')
print('You will have 10 attempts to guess a 3-digit number.')
count = 9
while True:
    try:
        guess_number = int(input('Enter your guess here:'))
        if count == 0:
            print('You failed. Restart the program to try again.')
            break
        else:
            if guess_number == magic_number:
                print('Boya! You have guessed the MAGIC number!')
                break
            elif guess_number < magic_number:
                if guess_number > down_range:
                    print('Nice guess, but a bit bigger would be nicer.')
                else:
                    print('Not very good. Try a bigger one.')
                count -= 1
            elif guess_number > magic_number:
                if guess_number < up_range:
                    print('Nice guess, but a little smaller would be nicer.')
                else:
                    print('Not very accurate. Try a smaller one.')
                count -= 1
            continue
    except ValueError:
        print('Wrong input. Remember to type a number.')
        continue
        
