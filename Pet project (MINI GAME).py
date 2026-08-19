import random

score = 0
high_score = 0

play_again = 'yes'

while play_again == 'yes':

    while True:
        difficulty = input('Choose difficulty: easy, medium, hard: ').lower()

        if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
            break

        print('Please choose easy, medium or hard!')

    if difficulty == 'easy':
        number = random.randint(1, 50)
        attempts = 10

    elif difficulty == 'medium':
        number = random.randint(1, 100)
        attempts = 5

    elif difficulty == 'hard':
        number = random.randint(1, 200)
        attempts = 3

    attempts_used = 0

    while attempts_used < attempts:
        try:
            user_data = int(input('Enter a number: '))
        except:
            print('Please enter a number!')
            continue

        attempts_used = attempts_used + 1

        if user_data > number:
            print('Your number is bigger')

        if user_data < number:
            print('Your number is smaller')

        if user_data == number:
            if attempts_used == 1:
                score = score + 100
            elif attempts_used == 2:
                score = score + 80
            elif attempts_used == 3:
                score = score + 60
            elif attempts_used == 4:
                score = score + 40
            elif attempts_used == 5:
                score = score +20
            else:
                score = score + 10
            
            print('You guessed it!')
            if score > high_score:
                 high_score = score
                 print('new High Score!')
   
            print('Your score:', score) 
            print('High Score:', high_score)
            
            break
            

        if attempts_used == attempts and user_data != number:
            print('You lost!')
            print('The number was:', number)
            print('Your score:', score) 
           
    while True:
        play_again = input('Play again? yes/no: ').lower()

        if play_again == 'yes' or play_again == 'no':
           break
        print('Please enter yes or no!')
print('===============================')
print(' = = = = = GAME OVER = = = = = ')
print('Final score:', score)
print('High Score:', high_score)
print('Thanks for playing!')