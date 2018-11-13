from random import randint

# get a random number from 0 to 100
number = randint(0, 100)

# initialize a tentative counter
tentative = 1

# explain the game
print('Guess a number from 1 to 100 in 10 tentatives.\n')

# ask user for his first guess

# if guess > number give user the right info
if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')

# if guess < number give user the right info
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')

# else the number is correct
else:
    print('Congratulations ! You won.')
    exit()

# increment tentative by one
tentative += 1

# nice formatting
print('==================================\n')

# repeat the same cycle: tentative 2
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 3
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 4
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 5
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 6
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 7
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 8
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 9
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

tentative += 1
print('==================================\n')

# repeat the same cycle: tentative 10
print('Guess the number(tentative n. ', tentative,  "):")
guess = int(input('Insert your number: '))

# if guess > number give user the right info and he losts
if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
    print('I am sorry! You lost.')

# if guess < number give user the right info and he losts
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
    print('I am sorry! You lost.')

# else the number is correct
else:
    print('Congratulations ! You won.')
    exit()

print('==================================\n')

