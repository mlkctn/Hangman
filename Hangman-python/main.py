import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
guessed_letters = []

print(logo)

display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. The word was:", chosen_word)

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
