import random

number = random.randint(1, 99)
guesses = 0

while guesses <= 5:
    guess = int(input("Enter the intiger between 1 to 99: "))
    guesses = guesses + 1
    print('No. of guesses are %d'%guesses)

if guess == number:
    print('you guessed it in: ', guesses +'guesses')

if guess < number:
    print('guess is low')
if guess > number:
    print('guess is high')
if guess != number:
    print('the secret number was', number) 