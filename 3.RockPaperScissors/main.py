#Tro choi oan tu ti

import random

def play ():
    user = input ("What's you choice? 'r' for rock , 'p' for paper, 's' for scissors \n ")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'It\'s a tie'

    # r>s, s>p, p>r
    if is_win (computer,user):
        return 'You win!'
    return 'You loss!'

def is_win (player, opponent):
    #return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player =='s' and opponent =='p') \
        or (player =='p' and opponent =='r'):
        return True

print(play())
    