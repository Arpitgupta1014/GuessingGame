import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

#Initializing count variable
count = 0

# main logic code
while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

# End of code

