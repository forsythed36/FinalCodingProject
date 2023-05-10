# This is a simple text-based numbers game.

# Set up the initial state of the game.
import random
random.seed()
guesses = 0
number = random.randint(1, 100)

# Greet the player and explain the rules of the game.
print("Welcome to the numbers game!")
print("I am thinking of a number between 1 and 100. Can you guess it in as few attempts as possible?")

# Loop until the player guesses the correct number.
while True:
  # Ask the player for their guess.
  guess = int(input("Enter your guess: "))

  # Check if the player's guess is correct.
  if guess == number:
    # If the guess is correct, end the game and print a success message.
    print("Congratulations, you guessed the number in {0} attempts!" .format(guesses))
    break

  # If the guess is not correct, give the player a hint and continue the game.
  elif guess < number:
    print("Your guess is too low. Try again.")
  elif guess > number:
    print("Your guess is too high. Try again.")
  guesses += 1

# End the game.
print("Thanks for playing!")