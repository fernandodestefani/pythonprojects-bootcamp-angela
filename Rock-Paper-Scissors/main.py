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
person_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
if person_choice == 0:
   print(rock)
elif person_choice == 1:
   print(paper)
else:
   print(scissors)
print('Computer choose:')
computer_choices = [rock, paper, scissors]
computer_choice = random.choice(computer_choices)
print(computer_choice)
if person_choice == 0 and computer_choice == rock:
   print('It is a draw')
elif person_choice == 0 and computer_choice == paper:
   print('You lose')
elif person_choice == 0 and computer_choice == scissors:
   print('You win')
elif person_choice == 1 and computer_choice == rock:
   print('You win')
elif person_choice == 1 and computer_choice == paper:
   print('It is a draw')
elif person_choice == 1 and computer_choice == scissors:
   print('You lose')
elif person_choice == 2 and computer_choice == rock:
   print('You lose')
elif person_choice == 2 and computer_choice == paper:
   print('You win')
else:
   print('It is a draw')