import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print('you guess too low. try again!')
        elif guess > random_number:
            print('you guess too high. try again!')

    print(f'you hit the number {random_number}!')

guess(10)