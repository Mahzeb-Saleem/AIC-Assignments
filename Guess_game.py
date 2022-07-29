import random
number=random.randint(0,10)
first_guess=input('Enter your 1st guess: ')
if first_guess==number:
    print('Congratulations! You Won')
else:
    second_guess=input('Enter your 2nd guess: ')
    if second_guess==number:
        print('Congratulations! You Won')
    else:
        third_guess=input('Enter your 3rd guess: ')
        if third_guess==number:
            print('Congratulations! You Won')
        else:
            print('Sorry! You lost')
