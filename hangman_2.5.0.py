#!/usr/bin/env python3
"""
Hangman Game v2.5.0
===================

Smooth ANSI-based screen clearing with fixed ASCII drawing.
Difficulty removed (fixed 6 guesses).

Version History:
- v1.0.0: Basic Hangman game logic
- v2.0.0: Added main menu system
- v2.1.0: Added multiple categories
- v2.2.0: Added random category option
- v2.3.0: Player name support + difficulty levels
- v2.4.0: Full screen clearing, fixed ASCII drawing,
           post-game screen, new game → main menu
- v2.5.0: Removed difficulty levels (fixed 6 guesses),
           straight gallows alignment,
           smooth screen clearing using ANSI escape codes
"""

import random
import time

# --------------------------------------------------
# Smooth Clear Screen (ANSI Escape Codes)
# --------------------------------------------------

def clear_screen():
    print("\033[2J\033[H", end="")
    time.sleep(0.12)

# --------------------------------------------------
# ASCII HANGMAN (STRAIGHT GALLOWS)
# --------------------------------------------------

HANGMAN_STAGES = [
    [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "  ======="
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "  ======="
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "  ======="
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "  ======="
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "  ======="
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "  ======="
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "  ======="
    ]
]

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def update_display(secret, display, guess):
    correct = False
    for i, ch in enumerate(secret):
        if ch == guess:
            display[i] = guess
            correct = True
    return correct, not correct

# --------------------------------------------------
# Display Functions
# --------------------------------------------------

def print_hangman(wrong, max_guesses, was_correct, was_wrong,
                  has_won, secret_word, display_word, guess, player):
    clear_screen()
    print(f"Player: {player} | Guess: {guess}\n")

    if has_won != 2:
        if was_correct:
            print("✅ Correct guess!")
        if was_wrong:
            print("❌ Incorrect guess!")
        print(f"⏳ Guesses left: {max_guesses - wrong}/{max_guesses}\n")
    else:
        print("🎉 YOU WON!")
        print(f"The word was: {secret_word}\n")

    print("Word:", ' '.join(display_word), "\n")

    stage = min(wrong, len(HANGMAN_STAGES) - 1)
    for line in HANGMAN_STAGES[stage]:
        print(line)

    if wrong >= max_guesses:
        print(f"\n💀 GAME OVER, {player}")
        print(f"The word was: {secret_word}")

def print_final_screen(wrong, max_guesses, secret_word, player, won):
    clear_screen()
    print(f"Player: {player}\n")

    if won:
        print("🎉 YOU WON!")
        stage = 0
    else:
        print("💀 GAME OVER")
        print(f"The word was: {secret_word}")
        print(f"You used {wrong}/{max_guesses} guesses")
        stage = 6

    print("\nWord:", ' '.join(['_'] * len(secret_word)), "\n")

    for line in HANGMAN_STAGES[stage]:
        print(line)

    input("\nPress Enter to continue...")

# --------------------------------------------------
# Game Data
# --------------------------------------------------

CATEGORIES = {
    "🍎 Fruits": ["banana", "orange", "papaya", "avocado", "grapes"],
    "🐘 Animals": ["elephant", "giraffe", "kangaroo", "penguin"],
    "🌍 Countries": ["india", "canada", "germany", "japan"],
    "🎬 Hollywood": ["inception", "matrix", "gladiator"],
    "🇮🇳 Indian Movies": ["dangal", "bahubali", "lagaan"],
    "💻 Programming": ["python", "java", "function", "variable"]
}

MAX_GUESSES = 6

# --------------------------------------------------
# Menus
# --------------------------------------------------

def get_player_name():
    clear_screen()
    while True:
        name = input("👤 Enter your name: ").strip()
        if name:
            return name.capitalize()

def show_main_menu():
    clear_screen()
    print("🎮 HANGMAN v2.5.0")
    print("=" * 40)
    for i, key in enumerate(CATEGORIES, start=1):
        print(f"{i}. {key}")
    print(f"{len(CATEGORIES) + 1}. 🎲 Random")
    print(f"{len(CATEGORIES) + 2}. Exit")
    return input("\nEnter choice: ").strip()

# --------------------------------------------------
# Core Game Logic
# --------------------------------------------------

def play_hangman(words, category, player):
    secret = random.choice(words)
    display = ['_'] * len(secret)
    wrong = 0
    has_won = 1

    while wrong < MAX_GUESSES and has_won < 2:
        print_hangman(wrong, MAX_GUESSES, False, False,
                      has_won, secret, display, "", player)

        guess = input("\nEnter a letter: ").lower().strip()

        if not is_valid_guess(guess):
            continue

        was_correct, was_wrong = update_display(secret, display, guess)

        if was_wrong:
            wrong += 1
        if ''.join(display) == secret:
            has_won = 2

        print_hangman(wrong, MAX_GUESSES, was_correct, was_wrong,
                      has_won, secret, display, guess, player)

    print_final_screen(wrong, MAX_GUESSES, secret, player, has_won == 2)

# --------------------------------------------------
# Main
# --------------------------------------------------

def main():
    player = get_player_name()

    while True:
        choice = show_main_menu()
        keys = list(CATEGORIES.keys())

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(keys):
                play_hangman(CATEGORIES[keys[choice - 1]], keys[choice - 1], player)
            elif choice == len(keys) + 1:
                key = random.choice(keys)
                play_hangman(CATEGORIES[key], key, player)
            elif choice == len(keys) + 2:
                clear_screen()
                print(f"Thanks for playing Hangman v2.5.0, {player}! 👋")
                break

if __name__ == "__main__":
    main()