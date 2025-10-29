'''
This is main function for a multilingual typing master program.

This function does following tasks:
1. Show welcome message.
2. Provide process to login or create account by inputs username and password.
3. Once login successfully, it provides process to:
    - Show user's information including username, password, as well as best score in each language and timer.
    - Show leaderboard based on language and timer, order by most word correct.
    - Start the game.
'''

# Library imports
from user import User
from leaderboard import load_leaderboard, show_leaderboard, update_leaderboard
from game import start_game

# Main function
def main():

    # Welcome message
    print(f'===== {'Multilingual Typing Master':^40} =====')
    print(f'===== {'Created by: Fauzan Rozin / 550618182':^40} =====')

    # Main process
    while True:

        # Process to login or create account
        is_login = False # Login status
        print('\nPlease select an option:')
        print('1. Login')
        print('2. Create Account')
        print('3. Exit')
        option = input('\nEnter option (1, 2 or 3): ')

        if option == '1': # Login
            username = input('\nEnter username: ')
            password = input('Enter password: ')
            user = User.load_user_from_files(username)
            if user and user.password == password:
                is_login = True
                print(f'\nLogin successful, welcome, {user.username}!')
            else:
                print('\nInvalid username or password, please try again!')

        elif option == '2': # Create account
            username = input('\nEnter desired username: ')
            password = input('Enter desired password: ')
            user = User.load_user_from_files(username)
            if user:
                print(f'\nAccount with username "{username}" already exists, please create another username!')
            else:
                new_user = User(username, password)
                new_user.save_user_to_files()
                print(f'\nAccount created successfully, you can now login, {username}!')

        elif option == '3': # Exit
            print('\nExiting the program, goodbye!')
            break

        else:
            print('\nInvalid option, please enter 1, 2 or 3!')

        # Once login successfully, show user's information, leaderboard or start the game
        while is_login:
            print('\nPlease select an option:')
            print('1. View Your Information')
            print('2. View Leaderboard')
            print('3. Start the Game')
            print('4. Logout')
            print('5. Exit')
            option = input('\nEnter option (1, 2, 3, 4 or 5): ')

            if option == '1': # View your information
                print(user)

            elif option == '2': # View leaderboard
                language = input('\nEnter language (indonesian/english): ').lower()
                timer = input('Enter timer duration (30/60 seconds): ')
                if language in ['indonesian', 'english'] and timer in ['30', '60']:
                    leaderboard = load_leaderboard(language, timer) # Load leaderboard data
                    show_leaderboard(leaderboard) # Show leaderboard data
                else:
                    print('\nInvalid language or timer duration, please try again!')

            elif option == '3': # Start the game
                language = input('\nEnter language (indonesian/english): ').lower()
                timer = input('Enter timer duration (30/60 seconds): ')
                if language in ['indonesian', 'english'] and timer in ['30', '60']:
                    words_correct = start_game(language, timer) # Start the game with selected language and timer
                    is_satisfied = user.set_best_score(language, timer, words_correct) # Check and set best score if satisfied
                    if is_satisfied:
                        user.update_user_in_files() # Update user data in files/user.csv
                    update_leaderboard(user.username, language, timer, words_correct) # Update leaderboard data
                else:
                    print('\nInvalid language or timer duration, please try again!')

            elif option == '4': # Logout
                print(f'\nLogging out, goodbye, {user.username}!')
                break

            elif option == '5': # Exit
                print('\nExiting the program, goodbye!')
                return
            
            else:
                print('\nInvalid option, please enter 1, 2, 3, 4 or 5!')

# Main function call
if __name__ == "__main__":
    main()