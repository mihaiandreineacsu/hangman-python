# Hangman Game in Python

This project is a command-line implementation of the classic Hangman game, where players attempt to guess a randomly chosen word within a limited number of attempts. It includes customizable options for difficulty and word selection.

## Features

- **Customizable Attempts**: Set the maximum number of incorrect guesses allowed via command-line arguments.
- **Word List Input**: Option to provide a custom text file containing words for the game.
- **Random Word Selection**: Words are selected randomly from a predefined list or a user-provided word list.
- **Dynamic Word Display**: Displays the current progress of the guessed word, showing underscores (_) for unguessed letters.
- **Input Validation**: Ensures that guesses are single alphabetic characters and provides feedback for invalid or repeated inputs.

## Requirements

- Python 3.7 or higher

## Installation

```bash
# Clone the repository:
git clone https://github.com/your-username/hangman-python.git
cd hangman-python
# Ensure Python is installed on your system:
python --version
```

## Usage

Run the game directly from the command line:

```bash
python hangman.py
```

## Optional Arguments

`--max_attempts`: Set the maximum number of attempts to guess the word (default is 7).
`--wordlist`: Provide a path to a text file containing custom words (one word per line).

Example:

```bash
python hangman.py --max_attempts 5 --wordlist custom_words.txt
```

## Word List Format

If you want to provide your own word list, ensure:

- The file has a `.txt` extension.
- Each word is on a separate line.
- Only alphabetic words are included.

Example (`custom_words.txt`):

```yaml
python
django
hangman
code
keyboard
```

## How to Play

1. The game will display the word to be guessed with underscores (_) representing unguessed letters.
1. Enter one letter at a time to guess the word.
1. You will be notified if the guess is correct or incorrect:
    - Correct Guess: The letter is revealed in the word.
    - Incorrect Guess: The number of remaining attempts decreases.
1. Win the game by guessing all the letters in the word before running out of attempts.

## Example Gameplay

```yaml
Word: _ _ n g m _ n
Guess a letter: h
Correct guess. Attempts remaining 6
Word: h _ n g m _ n
Guess a letter: z
Wrong guess. Attempts remaining 5
Word: h _ n g m _ n
...
```
