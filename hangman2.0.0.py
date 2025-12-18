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
    
    print(' '.join(display_word))
    print()
    
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

FRUITS = [
    "banana", "grapes", "orange", "papaya", "strawberry", "watermelon",
    "apricot", "avocado", "blueberry", "cantaloupe", "cranberry",
    "grapefruit", "honeydew", "raspberry", "tangerine", "blackcurrant",
    "boysenberry", "gooseberry", "kumquat", "loganberry", "nectarine",
    "passionfruit", "plantain", "pomegranate"
]

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def update_display(secret_word, display_word, guess):
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

def show_main_menu():
    print("\n" + "="*40)
    print("         HANGMAN GAME")
    print("="*40)
    print("1. Play")
    print("2. Exit")
    print("="*40)
    return input("Enter choice (1-2): ").strip()

def show_game_menu():
    print("\n" + "-"*30)
    print("GAME OPTIONS")
    print("-"*30)
    print("1. Continue")
    print("2. New Game")
    print("3. Exit")
    print("-"*30)
    return input("Enter choice (1-3): ").strip()

def play_hangman():
    secret_word = random.choice(FRUITS)
    display_word = ['_'] * len(secret_word)
    
    print("welcome to hangman: ")
    print()
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
        print("\n[Type 'menu' anytime to open game menu]")
        guess = input("enter your guess: ").lower().strip()
        
        # Mid-game menu option
        if guess == 'menu':
            choice = show_game_menu()
            if choice == '2':  # New Game
                return True  # Signal to start new game
            elif choice == '3':  # Exit
                return False  # Signal to exit
            continue  # Back to guess input
        
        if not is_valid_guess(guess):
            print("Please enter a single letter!")
            continue
        
        was_correct, was_wrong = update_display(secret_word, display_word, guess)
        clear_screen()
        
        if ''.join(display_word) == secret_word:
            has_won += 1
        
        if was_wrong:
            wrong_guesses += 1
        
        print_hangman(wrong_guesses, was_correct, was_wrong, has_won, 
                     secret_word, display_word, guess)
        print()
        print()
    
    return True  # Game completed, show main menu

def main():
    while True:
        choice = show_main_menu()
        
        if choice == '1':
            play_again = True
            while play_again:
                play_again = play_hangman()
                if not play_again:  # Exit requested
                    break
                
                # Post-game menu
                print("\nGame Over! Great game! 🎮")
                print("\nWhat would you like to do?")
                print("1. Play Again")
                print("2. Exit")
                post_choice = input("Enter choice (1-2): ").strip()
                
                if post_choice == '2':
                    play_again = False
                    print("Thanks for playing Hangman! 👋")
        elif choice == '2':
            print("Thanks for playing Hangman! 👋")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()