import random
import math

# Taking range---->(lower,upper) as input from user
lower=int(input("Enter a number for lower boundary:"));
upper=int(input("Enter a number for upper boundary:"));

# Generating random number between upper and lower using random module
# This is the number, which the user should guess
guess_number_generated=random.randint(lower,upper);

# Generating number of chances, the user can use, based on  the range
chances=math.ceil(math.log(upper-lower+1,2))
print("You have {} chances to guess the number between {} and {}".format(chances,lower,upper))

# To count the number of chances used by the user
count=0

# using loop to continue the guessing chances until count==chances
while count<chances:
    count+=1 #Increment the count for every iteration
    user_guess_number=int(input("Guess a number:"))
    
    if user_guess_number == guess_number_generated:
        print("Congratulations, you guessed the number in {} try".format(count))
        break
    elif user_guess_number<guess_number_generated:
        print("You guesses too small!")
    elif user_guess_number>guess_number_generated:
        print("You guessed too big!")

# If chances to guess are finished
if count >= chances:
    print("The number is:",guess_number_generated)
    print("Better luck next time!")