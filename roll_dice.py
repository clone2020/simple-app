import random

min = 1
max = 6

roll = 'no'

user = random.randint(min, max)
computer = random.randint(min, max)

while roll == 'no' or roll == 'n':
    roll = input('should we roll the dice .. ? ')
    if roll == 'no' or roll == 'n':
        print('provide valid input ..!')

if user == computer:
    print('Draw')

if user > computer:
    print('user wins')
elif user < computer:
    print('computer wins')

print('user is {}'.format(user))
print('computer is {}'.format(computer))