# Importing the random module
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum attempts allowed
max_attempts = 3

# Function to display a welcome message
def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")
    
#Function for recurssive guessing
def guess_recurssive(attempts_left):
    # Get user input
    guess = int(input("\nGuess the number(between 1 and 10):"))
    
    #Check if the guess is correct
    if guess == secret_number:
        print("Congratulatons! You guessed the correct number! ")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left>1:
            #Make a recurssive call for another guess
            guess_recurssive(attempts_left-1)
        else:
            print(f"\nSorry, you couldnt guess the number. The correct number was {secret_number}.")
            
# Calling the function 
welcome_message()
guess_recurssive(max_attempts)
                        
#Using id() to get memory addresses
print(f"Memory address of Secret Number {secret_number} is: {id(secret_number)}")
            
        