# Hangman Game 🎮

A simple **command-line Hangman game** built with Python.  
Guess the letters, reveal the hidden word, and try to save the hangman before it’s too late!

---

## 📖 Introduction  

The Hangman Game is a Python-based terminal game where a player guesses letters to reveal a secret word.  
Each wrong guess progresses an ASCII-art drawing of a hangman. The game ends when:  

- ✅ The player guesses the word correctly (Win)  
- ❌ The hangman is fully drawn (Lose)  

This project is intended as a beginner-friendly Python exercise.  

---

## 🚀 Features  

- Interactive terminal-based gameplay  
- ASCII-art visualization of hangman stages  
- Random word selection from a word list  
- Tracks correct and incorrect guesses  
- Easily customizable (words, stages, rules)  

---

## 📂 Project Structure  
├── hangman_game.py # Main game logic
├── hangman_stages.py # ASCII art for wrong guesses
├── word_file.py # Word list
└── README.md # Project documentation


File Details  

- **hangman_game.py** → Runs the game loop, manages guesses, and checks win/lose conditions  
- **hangman_stages.py** → Stores ASCII-art drawings for each stage of wrong guesses  
- **word_file.py** → Contains or loads the word list used for random word selection  


Requirements  

- **Python 3.7+**  
- No external dependencies (only Python standard library)  


