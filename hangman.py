import random
import os
import sys

game_state = "Not finished"

with open(os.path.join(sys.path[0], 'words.txt'), 'r') as reader:
    alist = [line.rstrip() for line in reader]
    word = random.choice(alist)

hidden_word = ["_"] * len(word)


def find_all(a_string, cha):
    start = 0
    while True:
        start = a_string.find(cha, start)
        if start == -1: 
            return
        yield start
        start += len(cha)

guesses = 3
while "_" in hidden_word:
    guess = input("Guess a letter: ")
    
    if guess in word:
        indexes = list(find_all(word, guess))
        for item in indexes:
            hidden_word[item] = guess
    else:
        guesses -= 1
    print(f"Lives remaining: {guesses}")
    print(" ".join(hidden_word))
    if guesses < 1:
        print("You lost")
        break

correct = "".join(hidden_word)

if correct == word:
    print("You beat the noose!")