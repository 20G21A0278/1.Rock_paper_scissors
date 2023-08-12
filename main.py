import random
rock='''
     _______
___'    ____)
      (_____)
      (_____)
---.__(____)
'''
paper='''
    _______
---'   ____)____
          ______)
         ________)
        ________)
---.__________)
'''
scissors='''
    _______
---'   ____)____
         _______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user_choice=int(input('Enter your choice:Type 0 for Rock,1 for paper,2 for scissors.'))
if user_choice>=3 or user_choice<0:
    print('Entered invalid number')
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print('computer_choice:')
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice == 0 and user_choice == 2:
        print('You lose')
    elif user_choice == 0 and computer_choice == 2:
        print('You win')
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")

