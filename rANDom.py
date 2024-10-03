import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Choose the number between 1 and {x}: "))
        print(guess)

        if (guess > random_number):
            print("Oo oh! You are too high.")
        elif (guess < random_number):
            print("hmm! Too low.")

    print("Yay, You guessed it correctly!!")

guess(10)