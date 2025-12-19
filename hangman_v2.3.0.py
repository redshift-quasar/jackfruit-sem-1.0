#!/usr/bin/env python3
"""
Hangman Game v2.3.0
===================
Added player names and difficulty levels.

Version History:
- v1.0.0: Basic Python code
- v2.0.0: Menu system
- v2.1.0: Added multiple categories
- v2.2.0: Added random category option
- v2.3.0: Player names + difficulty levels
"""

import random
import os

def print_hangman(wrong_guesses, max_guesses, was_correct, was_wrong, has_won, secret_word, display_word, guess, player_name):
    print(f"Player: {player_name} | Guess: {guess}")
    print()
    
    if has_won != 2:
        if was_correct:
            print("✅ Correct guess!")
        if was_wrong:
            print("❌ Incorrect guess")
        print(f"⏳ Guesses left: {max_guesses - wrong_guesses}/{max_guesses}")
        print()
    else:
        print("🎉 You won!!!!! ")
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
        ["  +---+", "  |   |", "  O   |", "/|\\  |", "/ \\  |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "/|\\  |", "/ \\  |", "      |", "========="]
    ]
    
    stage_index = min(wrong_guesses, len(hangman_stages) - 1)
    for line in hangman_stages[stage_index]:
        print(line)
    
    if wrong_guesses >= max_guesses:
        print(f"\t💀 Game Over {player_name} :(")
        print(f"\tThe word was: {secret_word}")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

CATEGORIES = {
    "🍎 Fruits": [
        "banana", "grapes", "orange", "papaya", "strawberry", "watermelon",
        "apricot", "avocado", "blueberry", "cantaloupe", "cranberry",
        "grapefruit", "honeydew", "raspberry", "tangerine", "blackcurrant",
        "boysenberry", "gooseberry", "kumquat", "loganberry", "nectarine",
        "passionfruit", "plantain", "pomegranate"
    ],
    "🐘 Animals": [
        "elephant", "giraffe", "kangaroo", "penguin", "octopus", "flamingo",
        "cheetah", "rhinoceros", "hippopotamus", "chameleon", "platypus",
        "armadillo", "anteater", "narwhal", "axolotl", "lemur", "panda"
    ],
    "🌍 Countries": [
        "afghanistan", "brazil", "canada", "denmark", "egypt", "france",
        "germany", "hungary", "iceland", "japan", "kenya", "luxembourg",
        "monaco", "norway", "oman", "portugal", "qatar", "russia", "spain"
    ],
    "🎬 Hollywood Movies": [
        "inception", "matrix", "gladiator", "titanic", "avatar", "joker",
        "interstellar", "shrek", "frozen", "coco", "moana", "zootopia",
        "godfather", "casablanca", "pulp fiction"
    ],
    "🇮🇳 Indian Movies": [
        "dangal", "bahubali", "pk", "dhoom", "raazi", "dabbang",
        "lagaan", "dilwale", "sultan", "sanju", "padmaavat",
        "bajrangi", "bhaijaan", "gully boy", "kabir singh",
        "uri", "kesari", "war", "tanhaji", "83"
    ],
    "💻 Programming": [
        "python", "java", "cpp", "javascript", "html", "css", "sql",
        "algorithm", "function", "variable", "boolean", "integer", "array",
        "object", "class", "method", "loop", "condition"
    ]
}

DIFFICULTY_LEVELS = {
    "1": ("🟢 Easy", 8),
    "2": ("🟡 Medium", 6), 
    "3": ("🔴 Hard", 4)
}

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

def get_player_name():
    """Get player name with validation."""
    while True:
        name = input("\n👤 Enter your name: ").strip()
        if name and len(name) <= 15:
            return name.capitalize()
        print("Please enter a valid name (max 15 chars)")

def show_main_menu():
    print("\n" + "="*65)
    print("         🎮 HANGMAN GAME v2.3.0")
    print("="*65)
    print("1.  🍎 Fruits")
    print("2.  🐘 Animals") 
    print("3.  🌍 Countries")
    print("4.  🎬 Hollywood Movies")
    print("5.  🇮🇳 Indian Movies")
    print("6.  💻 Programming")
    print("7.  🎲 Random Category")
    print("8.  Exit")
    print("="*65)
    return input("Enter choice (1-8): ").strip()

def show_difficulty_menu():
    print("\n" + "-"*40)
    print("⚡ SELECT DIFFICULTY")
    print("-"*40)
    for key, (name, guesses) in DIFFICULTY_LEVELS.items():
        print(f"{key}. {name} ({guesses} wrong guesses allowed)")
    print("-"*40)
    return input("Enter choice (1-3): ").strip()

def show_game_menu():
    print("\n" + "-"*45)
    print("⚙️  GAME OPTIONS v2.3.0")
    print("-"*45)
    print("1. Continue")
    print("2. New Game")
    print("3. Exit")
    print("-"*45)
    return input("Enter choice (1-3): ").strip()

def get_category_words(choice):
    if choice == '7':  # Random category
        category_name = random.choice(list(CATEGORIES.keys()))
        return CATEGORIES[category_name], category_name
    else:
        categories_list = list(CATEGORIES.values())
        categories_names = list(CATEGORIES.keys())
        if '1' <= choice <= '6':
            return categories_list[int(choice) - 1], categories_names[int(choice) - 1]
    return None, ""

def play_hangman(category_words, category_name, player_name, max_guesses):
    secret_word = random.choice(category_words)
    display_word = ['_'] * len(secret_word)
    
    print(f"\n🎯 Category: {category_name} | Player: {player_name}")
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
    
    while wrong_guesses < max_guesses and has_won < 2:
        print("\n💡 [Type 'menu' anytime to open game menu]")
        guess = input("enter your guess: ").lower().strip()
        
        if guess == 'menu':
            choice = show_game_menu()
            if choice == '2':
                return True
            elif choice == '3':
                return False
            continue
        
        if not is_valid_guess(guess):
            print("Please enter a single letter!")
            continue
        
        was_correct, was_wrong = update_display(secret_word, display_word, guess)
        clear_screen()
        
        if ''.join(display_word) == secret_word:
            has_won += 1
        
        if was_wrong:
            wrong_guesses += 1
        
        print_hangman(wrong_guesses, max_guesses, was_correct, was_wrong, has_won, 
                     secret_word, display_word, guess, player_name)
        print()
        print()
    
    return True

def main():
    # Get player name once at start
    player_name = get_player_name()
    print(f"\n🎮 Welcome {player_name}! Let's play Hangman!")
    
    while True:
        choice = show_main_menu()
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            # Get difficulty
            diff_choice = show_difficulty_menu()
            if diff_choice not in DIFFICULTY_LEVELS:
                print("❌ Invalid difficulty! Using Medium.")
                diff_choice = '2'
            
            difficulty_name, max_guesses = DIFFICULTY_LEVELS[diff_choice]
            category_words, category_name = get_category_words(choice)
            
            play_again = True
            while play_again:
                play_again = play_hangman(category_words, category_name, player_name, max_guesses)
                if not play_again:
                    break
                
                print(f"\n🎉 Game Over {player_name}! Great game!")
                print("\nWhat would you like to do?")
                print("1. Play Again (same settings)")
                print("2. Main Menu")
                print("3. Exit")
                post_choice = input("Enter choice (1-3): ").strip()
                
                if post_choice == '2':
                    play_again = False
                elif post_choice == '3':
                    print(f"Thanks for playing Hangman v2.3.0, {player_name}! 👋")
                    return
        elif choice == '8':
            print(f"Thanks for playing Hangman v2.3.0, {player_name}! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 1-8.")

if __name__ == "__main__":
    main()