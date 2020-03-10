import time

name = input('what is your name ? ')

print('hello', name +' it is time to play hangman!')
print()

time.sleep(2)

print('start guessing ..')
time.sleep(1)

word = 'secret'

guesses = ''

turn = 10

while turn > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
            print('you won..')
            break
    guess = input('guess a charecter: ')
    guesses += guess
    if guess not in word:
        turn -= 1
        print('wrong')
        print('you have', + turn ,'more guesses')
        if turn == 0:
            print('you lose')