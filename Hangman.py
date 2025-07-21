import random

# List of 5 predefined words
WORDS = ['apple', 'tiger', 'house', 'train', 'plant']

def play_hangman():
    word = random.choice(WORDS).upper()   # Random word
    guessed_letters = set()               # Letters guessed so far
    correct_letters = set(word)           # Letters that need to be guessed
    incorrect_guesses = 0                 # Counter for wrong guesses
    max_incorrect = 6                     # Max incorrect guesses allowed

    print("\nWelcome to Hangman!")
    print("Word:", "_ " * len(word))

    while incorrect_guesses < max_incorrect and correct_letters:
        guess = input("\nEnter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            correct_letters.remove(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} tries left.")

        # Show current word status
        current_display = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord:", current_display)
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))

    # Game Over
    if not correct_letters:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

def main():
    while True:
        play_hangman()
        choice = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if choice != 'Y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
