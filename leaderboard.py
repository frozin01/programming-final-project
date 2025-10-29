'''
This is leaderboard module for handling leaderboard-related processes.

This module has following functions:
- sort_leaderboard: Sort leaderboard data by words correct in descending order.
- load_leaderboard: Load leaderboard data from files/leaderboard/leaderboard_<language>_<timer>.csv and return as list of dictionaries.
- show_leaderboard: Show leaderboard data.
- update_leaderboard: Update leaderboard data in files/leaderboard/leaderboard_<language>_<timer>.csv.
'''

# sort_leaderboard function
def sort_leaderboard(leaderboard):
    try:
        leaderboard_sorted = sorted(leaderboard, key=lambda d: d['words_correct'], reverse=True) # Source: https://stackoverflow.com/questions/72899/how-can-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
    except Exception as e:
        print(f'Error: {e}')
    return leaderboard_sorted

# load_leaderboard function
def load_leaderboard(language, timer):
    leaderboard = []
    column_handler = 0
    try:
        with open(f'files/leaderboard/leaderboard_{language}_{timer}.csv', 'r') as f:
            for line in f:
                if column_handler == 0: # Skip header line
                    column_handler += 1
                    continue
                line_list = line.split(',')
                line_username = line_list[0]
                line_words_correct = int(line_list[1])
                leaderboard.append({'username': line_username, 'words_correct': line_words_correct})
    except Exception as e:
        print(f'Error: {e}')
    return leaderboard

# show_leaderboard function
def show_leaderboard(leaderboard):
    try:
        print(f'{"Rank":<6}{"Username":<20}{"Words Correct":<15}')
        for index, value in enumerate(leaderboard):
            print(f'{index + 1:<6}{value["username"]:<20}{value["words_correct"]:<15}')
    except Exception as e:
        print(f'Error: {e}')

# update_leaderboard function
def update_leaderboard(username, language, timer, words_correct):
    # Add new record (username, words_correct) to leaderboard
    try:
        with open(f'files/leaderboard/leaderboard_{language}_{timer}.csv', 'a') as f:
            f.write(f'{username},{words_correct}\n')
    except Exception as e:
        print(f'Error: {e}')
    
    # Read existing leaderboard and sort it
    leaderboard = load_leaderboard(language, timer)
    leaderboard_sorted = sort_leaderboard(leaderboard)

    # Write sorted leaderboard
    try:
        with open(f'files/leaderboard/leaderboard_{language}_{timer}.csv', 'w') as f:
            f.write('username,words_correct\n') # Write header line
            for entry in leaderboard_sorted:
                f.write(f'{entry["username"]},{entry["words_correct"]}\n') # Write each entry
    except Exception as e:
        print(f'Error: {e}')