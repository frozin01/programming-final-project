'''
This is game module for handling game-related processes.

This module has following functions:
- start_game: Start the typing game based on selected language and timer.
'''

# Library imports
import time
import random
from language import load_language

# start_game function
def start_game(language, timer):

    # Prepare the game
    language_data = load_language(language) # Load language data
    words_correct = 0
    print(f'\nStarting game in {language.capitalize()} for {timer} seconds!')
    
    # During the game
    input('Get ready! Press Enter to start!')
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < int(timer):  
        # Word appears
        if language == 'english':
            word_pair = random.choice(language_data)
            word = word_pair[0]
            print(f'\nType the word: {word}')
        else: # Indonesian
            word_pair = random.choice(language_data)
            word = word_pair[0]
            print(f'\nType the word: {word}')
        # User typing
        user_input = input('Your input: ')
        if user_input == word:
            words_correct += 1
            print('Correct!')
        else:
            print('Incorrect!')
        elapsed_time = time.time() - start_time

    # After the game
    print(f'\nTime is up! You typed {words_correct} words correctly.')
    return words_correct