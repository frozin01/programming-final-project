'''
This is game module for handling game-related processes.

This module has following functions:
- start_game: Start the typing game based on selected language and timer.
- countdown_timer: Countdown timer for starting the game.
'''

# Library imports
import time
import random
from language import load_language

# countdown_timer function
def countdown_timer(seconds):
    try:
        if seconds <= 0:  # base case
            print('Go!')
            return
        print(f'Starting in {seconds}...')
        time.sleep(1)
        countdown_timer(seconds - 1)  # recursive call
    except Exception as e:
        print(f'Error: {e}')

# start_game function
def start_game(language, timer):

    # Prepare the game
    language_data = load_language(language) # Load language data
    words_correct = 0
    print(f'\nStarting game in {language.capitalize()} for {timer} seconds!')
    
    # During the game
    input('Get ready! Press Enter to start!')
    countdown_timer(5) # Countdown before starting the game
    start_time = time.time()
    elapsed_time = 0
    try:
        while elapsed_time < int(timer):  
            # Word appears
            if language == 'english':
                word_pair = random.choice(language_data)
                word = word_pair.lower()
                print(f'\nType the word: {word}')
            else: # Indonesian
                word_pair = random.choice(language_data)
                word = word_pair[0].lower()
                translation = word_pair[1].lower()
                print(f'\nType the word: {word} =============== (English: {translation})')
            # User typing
            user_input = input('Your input: ').lower()
            if user_input == word:
                words_correct += 1
                print('Correct!')
            else:
                print('Incorrect!')
            elapsed_time = time.time() - start_time
    except Exception as e:
        print(f'Error: {e}')

    # After the game
    print(f'\nTime is up! You typed {words_correct} words correctly.')
    return words_correct