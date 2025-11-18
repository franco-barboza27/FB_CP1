import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 1
    game_over = False
    while not game_over:

        guess = int(input("Enter your guess: "))


        if guess > 100:

            print("Hey! That number is bigger than 100.")
        elif guess < 1:

            print("Hey! That number is smaller than 1!")
        elif attempts >= max_attempts:

            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            print("Game Over")
            game_over = True
        elif guess == number_to_guess:

            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:

            print("Too high! Try again.")
            attempts += 1
        elif guess < number_to_guess:

            print("Too low! Try again.")  
            attempts += 1
        else:
            "Your input did not match the format"
    print("Thanks for playing!")
start_game()

# not an error but please add more white space next time :^O

# (currently) line 17 the second if statement was "if", should have been "elif" (not best syntax)
# (currently) line 27 continue should be an "else" (not best syntax)

# line 5 var can be correct_num it's more descriptive

# line 29 thanks for playing fits both outcomes a bit better

# line 28 and 16 earlier it was looping infinitely since "attempts" wasn't changing, you need to add 1 to attempts each iteration (logic error)

# line 14-19, before your user could guess outside of the range. (logic error)

# guess wasn't an int (runtime error)