import random

def computer_roll():
    computer_number = random.randint(1,100)
    return computer_number
    

def main():
    name = input('Hello! What is your name?\n')

    greet_player = name
    print(greet_player + ' Can you guess the number that I am thinking of?\n')

    user_guess = int(input('Enter a number\n'))

    if user_guess == computer_roll:
        print(greet_player + ' That is correct great job!')

    else:
        print('Not quite, try again!\n')
main()
