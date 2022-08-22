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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice <0:
    print("You typed an invalid answer, you loose.")
else:
    print("Users choice")
    print(game_images[user_choice])
    print("\n\n\n")
    print("Computer's choice")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("The computer wins")
    elif computer_choice > user_choice:
        print("The computer wins")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It is a draw")

