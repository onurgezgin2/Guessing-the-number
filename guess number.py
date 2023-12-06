import random
def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess<random_num:
            print('Sorry,guess again.Too low.')
        elif guess>random_num:
            print('Sorry,guess again.Too high.')
    print(f'yay,congrats you have guess the number {random_num} correctly!!')
guess(100)
