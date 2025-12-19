import random
import os

def print_hangman(wrong_guesses, was_correct, was_wrong, has_won, secret_word, display_word, guess):
    print(f"Your guess: {guess}")
    print()
    
    if has_won != 2:
        if was_correct:
            print("Correct guess!")
        if was_wrong:
            print("Incorrect guess")
        print()
    else:
        print("You won!!!!! ")
        print(f"The word was: {secret_word}")
        print()
    
    # Show current word progress
    print(' '.join(display_word))
    print()
    
    # Hangman stages
    hangman_stages = [
        ["  +---+", "  |   |", "      |", "      |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "      |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "  |   |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "/|   |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "/|\\  |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "/|\\  |", "/    |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "/|\\  |", "/ \\  |", "      |", "========="]
    ]
    
    if wrong_guesses < 6:
        for line in hangman_stages[wrong_guesses]:
            print(line)
    else:
        for line in hangman_stages[6]:
            print(line)
        print("\tGame Over :(")
        print(f"\tThe word was: {secret_word}")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Fruits list (all lowercase for consistency)
FRUITS = [
    "banana", "grapes", "orange", "papaya", "strawberry", "watermelon",
    "apricot", "avocado", "blueberry", "cantaloupe", "cranberry",
    "grapefruit", "honeydew", "raspberry", "tangerine", "blackcurrant",
    "boysenberry", "gooseberry", "kumquat", "loganberry", "nectarine",
    "passionfruit", "plantain", "pomegranate"
]

def is_valid_guess(guess):
    """Check if input is a single alphabetic character."""
    return len(guess) == 1 and guess.isalpha()

def update_display(secret_word, display_word, guess):
    """Update display array based on guess (exact original logic)."""
    was_correct = False
    was_wrong = False
    
    for i, char in enumerate(secret_word):
        if guess == char:
            was_correct = True
            display_word[i] = guess
            was_wrong = False
        else:
            was_wrong = True
            if was_correct:
                was_wrong = False
    
    return was_correct, was_wrong

def play_hangman():
    # Pick random word
    secret_word = random.choice(FRUITS)
    display_word = ['_'] * len(secret_word)
    
    print("welcome to hangman: ")
    print()
    
    # Show initial empty hangman
    print("  +---+")
    print("  |   |")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")
    print()
    
    print("the word is: ", end="")
    print(' '.join(display_word))
    print()
    
    wrong_guesses = 0
    has_won = 1
    
    while wrong_guesses < 6 and has_won < 2:
        guess = input("enter your guess: ").lower().strip()
        
        if not is_valid_guess(guess):
            print("Please enter a single letter!")
            continue
        
        was_correct, was_wrong = update_display(secret_word, display_word, guess)
        clear_screen()
        
        # Check win condition
        if ''.join(display_word) == secret_word:
            has_won += 1
        
        if was_wrong:
            wrong_guesses += 1
        
        print_hangman(wrong_guesses, was_correct, was_wrong, has_won, 
                     secret_word, display_word, guess)
        print()
        print()

if __name__ == "__main__":
    play_hangman()
