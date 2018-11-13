from random import randint

# get a random number from 0 to 100
number = randint(0, 100)

# initialize a tentative counter
tentative = 1

# initialite a loop condition
loosing = True

# explain the game
print('Guess a number from 1 to 100 in 10 tentatives.\n')

# while loosing is true
while loosing:

    # ask user for his guess
    print('Guess the number(tentative n. ', tentative,  "):")
    guess = int(input('Insert your number: '))

    # if guess > number give user the right info
    if guess > number:
        print('Your guess (' + str(guess) + ') is higher then the number')
    
    # if guess < number give user the right info
    elif guess < number:
        print('Your guess (' + str(guess) + ') is lower than the number')

    # else the number is correct
    else:
        print('Congratulations! You won.')
        loosing = False

    # increment tentative by one
    tentative += 1

    # if tentative has passed 10 stop the loop and communicate the user he losts
    if tentative > 10:
        print('I am sorry! You lost.')
        loosing = False

    # nice formatting
    print('==================================\n')
