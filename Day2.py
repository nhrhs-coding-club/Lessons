


# Guessing Game

import random

print("\n-----------------------------------------")
print("Welcome to the Guessing Game\n\n")


number = random.randrange(10)

user_input = -1


def MakeAGuess():
	user_input = int(input("Guess a number (-1 to quit): "))

	if user_input == -1:
		print("Thanks for playing!")
		return True
	elif user_input == number:
		print("Nice, you got it dood.")
		return True
	elif user_input > number:
		print("Too high in the sky.")
		return False
	else:
		print("Too low, bro.")
		return False

	print("\n")	



while not MakeAGuess():
	continue

print("\n-----------------------------------------\n\n")























