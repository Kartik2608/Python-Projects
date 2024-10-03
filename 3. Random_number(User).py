import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low # it can also be high, coz high n low are same here!!
        feedback = input(f'Is the {guess} too high (H), too low (L) or correct (C)? ').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f'Yay! You guessed the number {guess} correctly.')


computer_guess(10)