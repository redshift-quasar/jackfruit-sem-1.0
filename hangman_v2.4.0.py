#!/usr/bin/env python3
"""
--
Hangman Game v2.4.0
===================
Full screen clearing with fixed ASCII drawing.

Version History:
- v1.0.0: Basic Python code
- v2.0.0: Menu system
- v2.1.0: Added multiple categories
- v2.2.0: Added random category option
- v2.3.0: Player names + difficulty levels
- v2.4.0: Full screen clearing + fixed ASCII + post-game ASCII + new game → main menu + difficulty retry + difficulty-based ASCII
"""

import random
import os
import time

def print_hangman(wrong_guesses, max_guesses, was_correct, was_wrong, has_won, secret_word, display_word, guess, player_name):
    clear_screen()
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
    
    # FIXED ASCII STAGES - PROGRESSION DEPENDS ON DIFFICULTY (max_guesses)
    hangman_stages = [
        # 0: Empty
        ["  +---+", "  |   |", "      |", "      |", "      |", "      |", "========="],
        # 1: Head
        ["  +---+", "  |   |", "  O   |", "      |", "      |", "      |", "========="],
        # 2: Head + body
        ["  +---+", "  |   |", "  O   |", "  |   |", "      |", "      |", "========="],
        # 3: Head + left arm (IMPROVED - natural angle)
        ["  +---+", "  |   |", "  O   |", " /|   |", "      |", "      |", "========="],
        # 4: Head + both arms
        ["  +---+", "  |   |", "  O   |", r"/|\  |", "      |", "      |", "========="],
        # 5: Head + arms + left leg
        ["  +---+", "  |   |", "  O   |", r"/|\  |", " /    |", "      |", "========="],
        # 6: FULL HANGMAN - shown for ALL losses
        ["  +---+", "  |   |", "  O   |", r"/|\  |", r"/ \  |", "      |", "========="]
    ]
    
    # NEW: Scale stage progression based on difficulty (max_guesses)
    if max_guesses == 8:  # Easy: slower progression (6 stages over 8 guesses)
        stage_index = min(wrong_guesses * 6 // 8, len(hangman_stages) - 1)
    elif max_guesses == 6:  # Medium: normal progression (6 stages over 6 guesses)
        stage_index = min(wrong_guesses, len(hangman_stages) - 1)
    else:  # Hard: faster progression (6 stages over 4 guesses)
        stage_index = min(wrong_guesses * 6 // 4, len(hangman_stages) - 1)
    
    for line in hangman_stages[stage_index]:
        print(line)
    
    # FULL HANGMAN + GAME OVER when ANY difficulty loses
    if wrong_guesses >= max_guesses:
        print(f"\n\t💀 GAME OVER {player_name} :(")
        print(f"\tThe word was: {secret_word}")
        print(f"\tYou had {max_guesses} guesses and used {wrong_guesses}")

def print_final_screen(wrong_guesses, max_guesses, secret_word, player_name, won):
    """Show final ASCII drawing with 'Press Enter to continue'"""
    clear_screen()
    print(f"Player: {player_name}")
    print()
    
    if won:
        print("🎉 You won!!!!! ")
        print(f"The word was: {secret_word}")
    else:
        print("💀 GAME OVER")
        print(f"The word was: {secret_word}")
        print(f"You had {max_guesses} guesses and used {wrong_guesses}")
    
    print()
    print(' '.join(['_'] * len(secret_word)))  # Show underscores for word length
    print()
    
    # NEW: Difficulty-based final hangman stage
    hangman_stages = [
        ["  +---+", "  |   |", "      |", "      |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "      |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", "  |   |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", " /|   |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", r"/|\  |", "      |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", r"/|\  |", " /    |", "      |", "========="],
        ["  +---+", "  |   |", "  O   |", r"/|\  |", r"/ \  |", "      |", "========="]
    ]
    
    # Show full hangman for loss (index 6), empty for win (index 0)
    stage_index = 6 if not won else 0
    for line in hangman_stages[stage_index]:
        print(line)
    
    print()
    input("Press Enter to continue...")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
    time.sleep(0.1)  # Smooth transition

CATEGORIES = {
    "🍎 Fruits": ["banana", "grapes", "orange", "papaya", "strawberry", "watermelon", "apricot", "avocado", "blueberry", "cantaloupe", "cranberry", "grapefruit", "honeydew", "raspberry", "tangerine", "blackcurrant", "boysenberry", "gooseberry", "kumquat", "loganberry", "nectarine", "passionfruit", "plantain", "pomegranate"],
    "🐘 Animals": ["elephant", "giraffe", "kangaroo", "penguin", "octopus", "flamingo", "cheetah", "rhinoceros", "hippopotamus", "chameleon", "platypus", "armadillo", "anteater", "narwhal", "axolotl", "lemur", "panda"],
    "🌍 Countries": ["afghanistan", "brazil", "canada", "denmark", "egypt", "france", "germany", "hungary", "iceland", "japan", "kenya", "luxembourg", "monaco", "norway", "oman", "portugal", "qatar", "russia", "spain"],
    "🎬 Hollywood Movies": ["inception", "matrix", "gladiator", "titanic", "avatar", "joker", "interstellar", "shrek", "frozen", "coco", "moana", "zootopia", "godfather", "casablanca", "pulp fiction"],
    "🇮🇳 Indian Movies": ["dangal", "bahubali", "pk", "dhoom", "raazi", "dabbang", "lagaan", "dilwale", "sultan", "sanju", "padmaavat", "bajrangi", "bhaijaan", "gully boy", "kabir singh", "uri", "kesari", "war", "tanhaji", "83"],
    "💻 Programming": ["python", "java", "cpp", "javascript", "html", "css", "sql", "algorithm", "function", "variable", "boolean", "integer", "array", "object", "class", "method", "loop", "condition"]
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
    clear_screen()
    print("🎮 HANGMAN GAME v2.4.0")
    print("="*50)
    while True:
        name = input("\n👤 Enter your name: ").strip()
        if name and len(name) <= 15:
            return name.capitalize()
        print("Please enter a valid name (max 15 chars)")

def show_main_menu():
    clear_screen()
    print("🎮 HANGMAN GAME v2.4.0")
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

def get_valid_difficulty():
    """Keep asking until valid difficulty input"""
    while True:
        diff_choice = show_difficulty_menu()
        if diff_choice in DIFFICULTY_LEVELS:
            _, max_guesses = DIFFICULTY_LEVELS[diff_choice]
            return max_guesses
        else:
            clear_screen()
            print("❌ Invalid difficulty! Please enter 1, 2, or 3.")
            input("Press Enter to try again...")

def show_difficulty_menu():
    clear_screen()
    print("⚡ SELECT DIFFICULTY")
    print("-"*50)
    for key, (name, guesses) in DIFFICULTY_LEVELS.items():
        print(f"{key}. {name} ({guesses} wrong guesses allowed)")
    print("-"*50)
    return input("Enter choice (1-3): ").strip()

def show_game_menu():
    clear_screen()
    print("⚙️  GAME OPTIONS v2.4.0")
    print("-"*50)
    print("1. Continue")
    print("2. New Game (Main Menu)")
    print("3. Exit")
    print("-"*50)
    return input("Enter choice (1-3): ").strip()

def show_post_game_menu(player_name):
    clear_screen()
    print(f"🎉 Game Over {player_name}! Great game!")
    print("\nWhat would you like to do?")
    print("1. Play Again (same settings)")
    print("2. Main Menu")
    print("3. Exit")
    return input("Enter choice (1-3): ").strip()

def get_category_words(choice):
    if choice == '7':
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
    
    clear_screen()
    print(f"🎯 Category: {category_name} | Player: {player_name} | Difficulty: {max_guesses} guesses")
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
                return "main_menu"
            elif choice == '3':
                return False
            continue
        
        if not is_valid_guess(guess):
            clear_screen()
            print("❌ Please enter a single letter!")
            input("Press Enter to continue...")
            print_hangman(wrong_guesses, max_guesses, False, False, has_won, 
                         secret_word, display_word, "", player_name)
            continue
        
        was_correct, was_wrong = update_display(secret_word, display_word, guess)
        
        if ''.join(display_word) == secret_word:
            has_won += 1
        
        if was_wrong:
            wrong_guesses += 1
        
        print_hangman(wrong_guesses, max_guesses, was_correct, was_wrong, has_won, 
                     secret_word, display_word, guess, player_name)
    
    won = (has_won == 2)
    print_final_screen(wrong_guesses, max_guesses, secret_word, player_name, won)
    
    return True

def main():
    player_name = get_player_name()
    
    while True:
        choice = show_main_menu()
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            max_guesses = get_valid_difficulty()
            category_words, category_name = get_category_words(choice)
            
            play_again = True
            while play_again:
                play_again = play_hangman(category_words, category_name, player_name, max_guesses)
                
                if play_again == "main_menu":
                    break
                
                if not play_again:
                    break
                
                post_choice = show_post_game_menu(player_name)
                
                if post_choice == '2':
                    play_again = False
                elif post_choice == '3':
                    clear_screen()
                    print(f"Thanks for playing Hangman v2.4.0, {player_name}! 👋")
                    input("Press Enter to exit...")
                    return
        elif choice == '8':
            clear_screen()
            print(f"Thanks for playing Hangman v2.4.0, {player_name}! 👋")
            input("Press Enter to exit...")
            break
        else:
            clear_screen()
            print("❌ Invalid choice! Please enter 1-8.")
            input("Press Enter to continue...")
            

if __name__ == "__main__":
    main()