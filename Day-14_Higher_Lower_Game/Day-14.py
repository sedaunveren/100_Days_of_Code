from game_data import data
from art14 import logo, vs
import random
import os

current_score = 0
play_game = True

B = random.choice(data)
while play_game:
    os.system('cls||clear')
    print(logo)
    if current_score >= 1:
        print(f"You're right! Current score: {current_score}")
    A = B
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    B = random.choice(data)
    print(f"Aganist B: {B['name']}, a {B['description']}, from {B['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if A['follower_count'] > B['follower_count']:
        if guess == 'A':
            current_score += 1
        else:
            os.system('cls||clear')
            print(logo)
            print(f"Sorry, that's wrong.Final score: {current_score}")
            play_game = False
    elif A['follower_count'] < B['follower_count']:
        if guess == 'A':
            os.system('cls||clear')
            print(logo)
            print(f"Sorry, that's wrong.Final score: {current_score}")
            play_game = False
        else:
            current_score += 1
    elif A['follower_count'] == B['follower_count']:
        B = random.choice(data)

  

  





