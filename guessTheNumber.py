import random

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input('Enter a number: '))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess < secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job, you guessed my number in ' + str(guessesTaken) + ' attempts.')
else:
    print('No the number that I am thinking of was ' + str(secretNumber) + '.')
    