'''
This is main function for a multilingual typing master program.

This function does following tasks:
1. Show welcome message.
2. Provide process to login or create account by inputs username and password.
3. Once login successfully, it provides process to:
    - Show user's best score in each language and timer duration.
    - Show leaderboard based on language and timer duration, order by most word correct.
    - Start the game.
'''

# Library imports
from user import User

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

        # Once login successfully, show user's best score, leaderboard or start the game
        while is_login:
            print('\nPlease select an option:')
            print('1. View Your Best Scores')
            print('2. View Leaderboard')
            print('3. Start the Game')
            print('4. Logout')
            print('5. Exit')
            option = input('\nEnter option (1, 2, 3, 4 or 5): ')
            if option == '1': # View best scores
                print('\nYour Best Scores:')
                print(f'- Indonesian 30 seconds: {user.best_indonesian_30} words correct')
                print(f'- Indonesian 60 seconds: {user.best_indonesian_60} words correct')
                print(f'- English 30 seconds: {user.best_english_30} words correct')
                print(f'- English 60 seconds: {user.best_english_60} words correct')
            elif option == '2': # View leaderboard
                print('\nLeaderboard feature is under development, please check back later!')
            elif option == '3': # Start the game
                print('\nGame feature is under development, please check back later!')
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