'''
Adapt the code to create a guessing game. Your game should ask the user for a username and greet him/her personally. 
Additionally, it should report a score (the number of guesses needed to guess the number correctly) at the end of the round. 
When the round is finished, your game should ask the user if he/she wants to play again.
'''

import random

def guessing_game(name, difficulty):
    '''
    Creates and runs a new guessing game. Users have to guess a number between 1 and {difficulty}
    '''
    randomNumber = random.randint(1, difficulty)
    guess = int(input(f"Hi {name}. I selected a secret number between 1 and {difficulty}. Try to guess it:\n>"))
    score = 1

    while guess != randomNumber:
        if guess < randomNumber:
            guess = int(input("Wrong - your number is too small! Guess again.\n>"))
        elif guess > randomNumber:
            guess = int(input("Wrong - your number is too big! Guess again.\n>"))
        score += 1
    print(40*'-')
    print(f"Good job {name}! You guessed {randomNumber} correctly")
    print(40*'-')


userName = input('Username: ')
print(f'Hi {userName}. Good luck!')

while True:
    maxNumber = int(input('Select difficulty (enter maximum number): '))
    guessing_game(name=userName, difficulty=maxNumber)
    again = input('Do you want to play again (y/n)?: ')
    if again != 'y':
        break
    print(3*'\n')


