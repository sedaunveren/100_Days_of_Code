import os
from art9 import logo
os.system('cls||clear')
print(logo)
print("Welcome to the secret auction program.")
bids = {}
con = True
while con:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    answer = input("Are there any other bidders? Type 'yes' or 'no': ")
    if answer == "yes":
        con = True
        os.system('cls||clear')
    elif answer == "no":
        con = False
max_price = 0
winner = ""
for bidders in bids:
    pric = bids[bidders]
    if pric > max_price:
        max_price = pric
        winner = bidders
print(f"The winner is {winner} with a bid of ${max_price}.")



