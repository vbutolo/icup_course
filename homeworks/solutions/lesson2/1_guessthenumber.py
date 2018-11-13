from random import randint

# get a random number from 0 to 100
number = randint(0, 100)

# initialize a attempt counter
attempt = 1

# explain the game
print('Guess a number from 1 to 100 in 10 attempts.\n')

# ask user for his first guess
guess = int(input('Insert your number: '))

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

# increment attempt by one
attempt += 1

# nice formatting
print('==================================\n')

# repeat the same cycle: attempt 2
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 3
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 4
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 5
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 6
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 7
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 8
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 9
print('Guess the number(attempt n. ', attempt,  "):")
guess = int(input('Insert your number: '))

if guess > number:
    print('Your guess (' + str(guess) + ') is higher then the number')
elif guess < number:
    print('Your guess (' + str(guess) + ') is lower than the number')
else:
    print('Congratulations ! You won.')
    exit()

attempt += 1
print('==================================\n')

# repeat the same cycle: attempt 10
print('Guess the number(attempt n. ', attempt,  "):")
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

