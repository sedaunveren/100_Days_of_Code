import random
from art12 import logo

print(logo)
EASY_MODE = 10
HARD_MODE = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulyt. Type 'easy' or 'hard': ")

num = random.randint(1,100)
def play_game(attemps):
    continue_game = True
    while continue_game:
        print(f"You have {attemps} attempts remaining to guess the number.")
        guess = int(input(f"Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {guess}")
            continue_game = False
        elif guess < num:
            print("Too low")
            print("Guess again.")
            attemps -= 1
            if attemps == 0:
                print("You've run out of guesses, you lose")
                continue_game = False
        elif guess > num:
            print("Too high")
            print("Guess again.")
            attemps -= 1
            if attemps == 0:
                print("You've run out of guesses, you lose")
                continue_game = False

if choice == "easy":
    play_game(EASY_MODE)
elif choice == "hard":
    play_game(HARD_MODE)



