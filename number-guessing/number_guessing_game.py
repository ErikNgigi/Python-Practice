import math
import random

# Inputs lower bound
lower_bound = int(input("Enter a number for the lower bound: "))

# Inputs higher bound
higher_bound = int(input("Enter a number for the higher bound: "))

# generate number in the higher and lower bounds
x = random.randint(lower_bound, higher_bound)

guesses = math.log(higher_bound - lower_bound + 1, 2)

print("\n\tYou've only ", round(guesses), " chances to guess the integer\n")

# Initialize number of guess
count = 0

# Calculate minimum number of guesses depending upon range
while count < guesses:
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulations you guessed correctly", count, " try")
        # Once guessed, will break loop
        break
    elif x > guess:
        print("You've guessed to small")
    elif x < guess:
        print("You've guessed to big")

# If guessing passes number of required guessed
if count >= guesses:
    # %d is a placeholder for an integer value, and % x
    print("\nThe number is %d" % x)
    print("\nBetter luck next time!")
