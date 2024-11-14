import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"Welcome to the HangMan's game, you start with {lives} lives ****************************".upper())
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have guess the {guess} letter")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        if lives == 0:
            game_over = True

            print(f"It was {chosen_word}. You lose!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
