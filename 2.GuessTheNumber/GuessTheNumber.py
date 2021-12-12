# Tro choi doan so

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int (input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
    print(f'Yeah, congrats. You have guessed the number {random_number} correctly!')

def computer_guess(x):
    low = 1
    hight = x
    feedback = ''
    while feedback != 'c':
        if low != hight:
            guess =  random.randint(low, hight)
        else:
            guess = low #
        feedback = input(f'Is {guess} too hight (H), too low (L), or correctly (C)')
        if feedback == 'h':
            hight = guess - 1
        elif feedback =='l':
            low =  guess + 1
    print(f'Yeah, congrats. You have guessed the number, {guess}, correctly!')

computer_guess(1000)
