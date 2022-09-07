import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

lives = 6

word = random.choice(word_list)

print(f"generated word : {word}")
print(f"No of lives : {lives}")

display = ["_" for _ in range(0, len(word))]


game_end = False
while not game_end:

    guess = input("Guess the word ").lower()

    if guess in display:
        print("word is already guessed")

    if guess not in word:
        print("wrong answer")
        lives -= 1

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter
            print(display)


    if "_" not in display:
        game_end = True

    if lives == 0:
        game_end = True

    print(f"No of lives : {lives}")
    print(stages[lives])