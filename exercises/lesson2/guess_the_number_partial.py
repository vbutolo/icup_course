number = int(input('Insert your number: '))

guess = int(input('Insert your guess: '))

# if guess > number give user the right info
if guess > number:
    print('Your guess (', guess, ') is higher then the number')

# if guess < number give user the right info
elif guess < number:
    print('Your guess (', guess, ') is lower than the number')

# else the number is correct
else:
    print('Congratulations! You won.')