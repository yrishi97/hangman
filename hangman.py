import random

def get_word():
    words = ['cryptocurrency', 'pizzazz', 'python', 'quizzical', 'hangman','easy','tough']
    return random.choice(words).upper()

def display_board(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def play_hangman():
    word = get_word()
    word_letters = set(word)  # unique letters in the word
    guessed_letters = set()   # correctly guessed letters
    wrong_guesses = set()     # wrongly guessed letters
    attempts = len(word)  # number of attempts (1 for each letter)
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and len(word_letters) > 0:
        # Display current state of the word
        print("\nWord:", display_board(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        print("Wrong guesses:", " ".join(wrong_guesses))
        
        # Take the user's guess
        guess = input("Guess a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
            continue
        
        # Check if the guessed letter is correct
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
    
    # End of the game
    if len(word_letters) == 0:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_hangman()
