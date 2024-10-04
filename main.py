import random
from hangman_art import stages, logo
from fruits import fruit_list
chosen_word = random.choice(fruit_list).lower()
display = '_' * len(chosen_word)
guessed_letters = []
lives = len(chosen_word) -2
print("Welcome to Hangman!")
print(logo)

while True:
    print(f'\nWord: {display}')
    print(f'lives: {lives}')
    guess = input("Guess the letters: ").lower()

    if guess in guessed_letters:
        print('You already guessed the letter. Try again')
        continue
    guessed_letters.append(guess)
    if guess not in chosen_word:
        lives -= 1
        print(f'Wrong Guess! Your lives remaining {lives}.')

    else:
        print('Correct Guess!')
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
    print(stages[lives])
    if "_" not in display:
        print(f'Congratulations! You guessed the correct word: {chosen_word}')
        break
    if lives == 0:
        print(f'Sorry you ranout the lives. The correct word was {chosen_word}')
        break