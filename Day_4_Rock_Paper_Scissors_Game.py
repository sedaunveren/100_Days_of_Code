## Rock, Paper, Scissors Game ##

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]
c = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
if c >= 3 or c < 0:
    print("You typed an invalid number, you lose!")
else:
    print("Your chose:")
    print(choice[c])

l = len(choice)
computer = random.randint(0,l-1)
print("Computer chose:")
print(choice[computer])


if c == 0 and computer == 0:
    print("It's a draw.")
elif c == 0 and computer == 1:
    print("You lose.")
elif c == 0 and computer == 2:
    print("You win.")
elif c == 1 and computer == 0:
    print("You win.")
elif c == 1 and computer == 1:
    print("It's a draw.")
elif c == 1 and computer == 2:
    print("You lose.")
elif c == 2 and computer == 0:
    print("You lose.")
elif c == 2 and computer == 1:
    print("You win.")
elif c == 2 and computer == 2:
    print("It's a draw.")

