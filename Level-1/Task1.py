import random

def number_guessing_game():
    num_to_guess = random.randint(1,50)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 50. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter Your Guess:"))
            attempts +=1

            if guess < num_to_guess:
                print("Too low! Try again.")
            elif guess > num_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please Enter a valid number :)")

number_guessing_game()
