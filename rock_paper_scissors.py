import random
computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('Tie the computer chose ' + computer_choice)
elif user_choice == 'rock' and computer_choice == "scissors":
    print('You win the computer chose ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win the computer chose ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win the computer chose ' + computer_choice)
else:
    print('you lose :P computer had ' + computer_choice)

 