import random

score = 0
high_score = 0
games_played = 0
wins = 0
losses = 0
total_score = 0
play_again = 'yes'


def update_high_score(score, high_score):
    if score > high_score:
        high_score = score
        print('New High Score!')

    return high_score
    
def show_statistics(games_played, wins, losses, high_score, total_score):
    print()
    print('========== STATISTICS ==========')
    print('Games played:', games_played)
    print('Wins:', wins)
    print('Losses:', losses)
    print('Best score:', high_score)

    if games_played > 0:
        average_score = total_score / games_played
        print('Average Score:', round(average_score, 2))
    else:
        print('Average Score = 0')

    print('===================================')
    
print('==============================')
print('      NUMBER GUESSING GAME')
print('==============================')

def main_menu():
    while True:
        print()
        print('1. Start Game')
        print('2. Rules')
        print('3. Stats')
        print('4. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            return 'start'

        elif choice == '2':
            print()
            print('RULES:')
            print('- Choose a difficulty.')
            print('- Guess the secret number.')
            print('- You have limited attempts.')
            print('- The faster you guess, the more points you get.')

        elif choice == '3':
            show_statistics(games_played, wins, losses, high_score, total_score)
            
        elif choice == '4':
            return 'exit'

        else:
            print('Please choose 1, 2, 3 or 4')

def choose_difficulty():
    
    while True:
        difficulty = input(
            'Choose difficulty: easy, medium, hard: '
        ).lower()

        if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
            return difficulty

        print('Please choose easy, medium or hard!')

def setup_game(difficulty):
    
    if difficulty == 'easy':
        number = random.randint(1, 50)
        attempts = 10

    elif difficulty == 'medium':
        number = random.randint(1, 100)
        attempts = 5

    elif difficulty == 'hard':
        number = random.randint(1, 200)
        attempts = 3

    return number, attempts

def play_game(number, attempts):
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
                score = 100
            elif attempts_used == 2:
                score = 80
            elif attempts_used == 3:
                score = 60
            elif attempts_used == 4:
                score = 40
            elif attempts_used == 5:
                score = 20
            else:
                score = 10
            print('You guessed it!')
            return score

        if attempts_used == attempts:
            print('You lost!')
            print('The number was:', number)
            return 0

while True:
    choice = main_menu()

    if choice == 'exit':
        break

    if choice == 'start':
        play_again = 'yes'

        while play_again == 'yes':
            difficulty = choose_difficulty()

            print('You chose:', difficulty)

            number, attempts = setup_game(difficulty)

            score = play_game(number, attempts)

            games_played = games_played + 1

            total_score = total_score + score
            
            if score > 0:
                wins = wins + 1
            else:
                losses = losses + 1

            print('Your score:', score)

            high_score = update_high_score(score, high_score)

            print('High Score:', high_score)

            while True:
                play_again = input('Play again? yes/no: ').lower()
                if play_again == 'yes' or play_again == 'no':
                     break
                print('Please enter yes or no!')

print('==============================')
print('        GAME OVER')
print('==============================')
print('Final score:', score)
print('High Score:', high_score)
print('Thanks for playing!')