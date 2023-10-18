'''
# Guessing Game Challenge

A program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is
 * within 10 of the number, return "WARM!"
 * further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is 
 * closer to the number than the previous guess return "WARMER!"
 * farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

'''
import random

random_num = random.randint(1, 100)

print('''
Welcome to the Guessing Game Challenge. 

Guess the number we have in mind, and we will tell you if you're close or not.
If you guess it right, you get 10 points!
''')

my_list = []  # Initialize list to store guesses

def check_diff(random_num, num2):
    my_list.append(num2)  # Store the new guess
    if num2 == random_num:
        return 'You guessed it right! It took you {} tries.'.format(len(my_list) - 1)
    elif len(my_list) == 1:
        if abs(random_num - num2) <= 10:
            return 'WARM!'
        else:
            return 'COLD!'
    else:
        prev_guess = my_list[-2]
        prev_diff = abs(random_num - prev_guess)
        current_diff = abs(random_num - num2)
        if current_diff < prev_diff:
            return 'WARMER!'
        else:
            return 'COLDER!'

while True:
    try:
        user_input = int(input("Please enter your guess: "))

        if user_input < 1 or user_input > 100:
            print('OUT OF BOUNDS')
            continue  # Continue to the next iteration

        result = check_diff(random_num, user_input)
        print(result)

        if result.startswith('You guessed it right!'):
            break  # End the game if the user guessed correctly

    except ValueError:
        print('Invalid input. Please enter a valid number.')



  
  