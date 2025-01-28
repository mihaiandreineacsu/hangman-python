import argparse
import random
import os

DEFAULT_ATTEMPTS = 7
WORDS = ["python", "django", "angular", "laptop", "server"]
MIN_ATTEMPTS = 1
MAX_ATTEMPTS = os.getenv("MAX_ATTEMPTS", DEFAULT_ATTEMPTS)
if MAX_ATTEMPTS < MIN_ATTEMPTS:
    MAX_ATTEMPTS = DEFAULT_ATTEMPTS


def get_words_list(words_list: str) -> list[str]:
    """
    Extracts the words from given "words_list" file path.

    Raises:

        argparse.ArgumentTypeError: If the given file does not exist, is empty or not a TXT file.

    Returns:

        list[str]: A list of words from the given "word_list" file path.
    """

    if not words_list.endswith(".txt"):
        raise argparse.ArgumentTypeError(f"File '{words_list}' is not a TXT file!")

    if not os.path.isfile(words_list):
        raise argparse.ArgumentTypeError(f"File '{words_list}' does not exist!")

    if os.path.getsize(words_list) == 0:
        raise argparse.ArgumentTypeError(f"File '{words_list}' is empty!")

    with open(words_list, "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    words = [word.lower() for word in words if word.isalpha()]
    return words


def init_args() -> argparse.Namespace:
    """
    Parses the arguments given when running the script.

    Accepted arguments are:
    - max_attempts: The maximal attempts to guess the word. (default: {MAX_ATTEMPTS})
    - wordlist: A Textfile containing words to randomly pick the in game word to guess. (optional)

    Returns:

        argparse.Namespace: Parsed arguments
    """

    parser = argparse.ArgumentParser(description="Play Hangman game")
    parser.add_argument(
        "--max_attempts",
        required=False,
        type=int,
        choices=range(MIN_ATTEMPTS, MAX_ATTEMPTS),
        default=MAX_ATTEMPTS,
        help=f"The maximal attempts to guess the word. (default: {MAX_ATTEMPTS})",
    )
    parser.add_argument(
        "--wordlist",
        required=False,
        type=get_words_list,
        help="A Textfile containing words to randomly pick the in game word to guess. (optional)",
    )

    return parser.parse_args()


def init_hangman() -> tuple[int, str]:
    """
    Initializes the game attempts and the word to guess.

    Returns

        tulpe[int, str]: remaining guess attempts and the word to guess.
    """

    args = init_args()
    in_game_attempts = args.max_attempts or MAX_ATTEMPTS
    in_game_word = random.choice(args.wordlist or WORDS)
    return in_game_attempts, in_game_word


def display_word(word: str, guesses: list[str]) -> str:
    """
    The word to guess showed to the player.
    Any guesses letters are displayed.
    Non guessed letters are showed as underscore "_".

    Returns
        str: a string that follows the patter '_ _ X _ Y _ _ Z'
    """

    word_to_display = ""
    for letter in word:
        letter_to_display = letter if letter in guesses else "_"
        word_to_display += letter_to_display + " "

    return word_to_display.strip()


def start_game(attempts: int, word: str):
    """
    Starts the game loop with given "attempts" to guess the given "word".

    The game ends if:
    - The player used up all given attempts. (Game Over!)
    - The player guessed the given word. (Game Won!)
    """

    guesses = []

    while True:

        word_to_display = display_word(word, guesses)
        print(f"Word: {word_to_display}")

        if attempts == 0:
            print("Game over! You have been hanged.")
            break

        if word == word_to_display.replace(" ", ""):
            print("Congratulation! You found the word and escaped hanging.")
            break

        char = input("Guess a letter: ").strip().lower()

        if len(char) > 1 or not char.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if char in guesses:
            print("You already guessed this letter! Try again.")
            continue

        if char not in word:
            attempts = attempts - 1
            guesses.append(char)
            print(f"Wrong guess. Attempts remaining {attempts}")
            continue

        print(f"Correct guess. Attempts remaining {attempts}")
        guesses.append(char)


def main():
    attempts, word = init_hangman()
    start_game(attempts, word)


if __name__ == "__main__":
    main()
