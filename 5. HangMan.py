import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "_" in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 3

    
    while len(word_letter) > 0 and lives > 0:

        print("You guessed: ", " ".join(used_letter))

        word_list = [i if i in used_letter else "_" for i in word]
        print("Guess: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word. ", lives, "left.")
        
        elif user_letter in used_letter:
            print("Try another guess.")
        
        else:
            print("Invalid Character.")

    if (lives == 0):
        print("Oo..oh! You died. The word was ", word, ".")
    else:
        print("Yay! You got the", word, "correctly.")
        
hangman()