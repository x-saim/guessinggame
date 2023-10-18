# Number Guessing Game (CLI Game)

Welcome to the Number Guessing Game! This is a command-line interface (CLI) game that challenges you to guess a randomly selected number from 1 to 100. The game provides feedback on the closeness of your guesses and tells you how many tries it took to guess the correct number.

## Rules

1. The game randomly selects a number between 1 and 100.
2. Your task is to guess the selected number.
3. The game provides feedback on the proximity of your guesses using the following cues:
   - "WARM!" if your guess is within 10 of the number.
   - "COLD!" if your guess is further than 10 away from the number.
   - "WARMER!" if your guess is closer to the number than your previous guess.
   - "COLDER!" if your guess is farther from the number than your previous guess.
4. When you guess the correct number, the game will inform you of your success and tell you how many tries it took.

## Usage

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed (Python 3 is recommended).
3. Run the `game.py` script using a Python interpreter.
4. Follow the on-screen instructions to make your guesses.
5. Keep guessing until you correctly guess the number.

```bash
python game.py
