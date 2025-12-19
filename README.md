# 🎮 Python Terminal Games Collection

A collection of two fun and interactive **Python terminal games**:

1. **Hangman v2.5.2** – Classic word guessing with categories and animations.  
2. **Tic Tac Toe AI** – Play against your friend or computer with multiple difficulty levels.

Each game runs directly in your terminal and uses only standard Python libraries.

---

## 🧩 Included Games

| Game | Description | Mode |
|------|--------------|------|
| **Hangman v2.5.2** | Word guessing game with categories, ASCII art, and player tracking. | Single player |
| **Tic Tac Toe AI** | 3x3 board game with single- and multiplayer options and adaptive difficulty. | 1–2 players |

---

## ⚙️ Requirements

- Python 3.6 or higher  
- Any terminal or console supporting **ANSI codes** (for Hangman effects)

Tested on macOS, Linux, and Windows (10+).

---

## 🚀 How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run either game directly:


---

## 🎯 Game 1: Hangman v2.5.2

A modernized version of the traditional Hangman word game with clean design and colorful feedback.

### 🆕 Latest Patch (v2.5.2)
- Bug fix: final screen now shows the full revealed word for win or loss.
- Small visual and text improvements.

### 🕹️ Features
- Multiple word **categories** (Fruits, Animals, Countries, Movies, Programming).
- **Random category** mode.
- **Smooth screen clearing** using ANSI escape codes.
- Clean **ASCII gallows** with straight alignment.
- Clear win/loss feedback and revealed word display.
- Simple and modular code structure for easy customization.


---

## 🎯 Game 2: Tic Tac Toe (with AI)

A 3x3 grid-based game supporting both single-player (vs computer) and two-player modes.

### 🤖 Difficulty Levels
- **Easy** – Makes random moves.  
- **Medium** – Tries to win or block player.  
- **Hard** – Uses a simple *minimax algorithm* for optimal play.

### 🧠 Game Logic Highlights
- Dynamic 3x3 board printed in terminal.  
- Detects all winning combinations (rows, columns, diagonals).  
- Validates user input to prevent invalid moves.  
- AI uses recursion and scoring to choose the best move in *hard* mode.  
- **Two-player mode** available for local multiplayer.

### 🕹️ How to Play
1. Start the game.
2. Choose **Single Player** or **Two Player** mode.
3. In single-player, choose difficulty: `easy`, `medium`, or `hard`.
4. Enter your move (1–9) based on board positions:
5. The first player uses **X**, and either the computer or second player uses **O**.  
6. The game declares the result automatically — win, loss, or draw.


---

## 🧰 Folder Structure

  📁 python-terminal-games/
│
├── hangman_v2.5.2.py # Hangman v2.5.2 script
├── tictactoe_v2.0.0.py # Tic Tac Toe with AI difficulties
└── README.md # This file


---

## 🧑‍💻 Developer Notes

- Both games are **entirely text-based** and rely on built-in libraries (`random`, `time`).
- The code is **modular, beginner-friendly, and easy to expand**.
- No external dependencies required.
- Designed for command-line interactivity and educational projects.

---

## 📄 License

This repository is open for educational and personal use.  
Feel free to modify, extend, or integrate the games with proper credit.

---

## 👋 Credits

Developed by **Atharva Patel and Brahmesh Bharti (Hangman) ; Basavaprabhu Salmani and Parjivin Raj (Tic Tac Toe)**  
Made with 🐍 Python and ❤️ for learning & fun!




