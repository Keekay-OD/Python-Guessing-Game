# This is a guess the number game by OmarDiaz using python 
import random
secretNumber = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')

#Ask the player to guess 6 times.
for guessesTaken in range(1, 7,):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break   # This condtion is the correcct guess!

if guess == secretNumber:
    print('Good Job! You guessed my number in ' + str(guessesTaken) +' guesses!')
else:
    print('Nope. The number is was thinking of was ' + str(secretNumber))
