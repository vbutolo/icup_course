from random import randint

number = randint(0, 100)
tentative = 1

loosing = True

print('Guess a number from 1 to 100 in 10 tentatives.\n')

while loosing:
    print('Guess the number(tentative n. ', tentative,  "):")
    guess = int(input('Insert your number: '))

    if guess > number:
        print('Your guess (' + str(guess) + ') is higher then the number')
    elif guess < number:
        print('Your guess (' + str(guess) + ') is lower than the number')
    else:
        print('Congratulations! You won.')
        loosing = False

    tentative += 1

    if tentative > 10:
        print('I am sorry! You lost.')
        loosing = False

    print('==================================\n')
