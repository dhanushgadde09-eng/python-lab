# Number Guessing Game

import random

secret_number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        print("Number of attempts:", attempts)
        break

output
Guess the number between 1 and 100.
Enter your guess: 76
Too low! Try again.
Enter your guess: 45
Too low! Try again.
Enter your guess: 98
Too high! Try again.
Enter your guess: 32
Too low! Try again.
