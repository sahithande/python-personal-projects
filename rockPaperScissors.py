import random, sys

print('ROCK, PAPER, SCISSORS')

# these variables keep track of the number of wins, ties and losses.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print(f"{wins} Wins, {ties} Ties, {losses} Losses")
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Enter one among r, p, s or q')

    # Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)
    # Display what the computer chose
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    # Display the record of win, loss and tie
    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose.')
        losses += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose.')
        losses += 1