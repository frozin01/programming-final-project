'''
This is user class for storing user information and handling user-related processes.

This class has following methods:
- __init__: Initialize user object with username and password.
- __str__: Return string formatted of user object.
- save_user_to_files: Save user data to files/user.csv.
- load_user_from_files: Load user data from files/user.csv and return as user objects.
- set_best_score: Set best score for specific language and timer.
- update_user_in_files: Update user data in files/user.csv.
'''

# User class
class User:

    # __init__ method
    def __init__(self, username, password, best_indonesian_30=0, best_indonesian_60=0, best_english_30=0, best_english_60=0):
        self.username = username
        self.password = password
        self.best_indonesian_30 = best_indonesian_30
        self.best_indonesian_60 = best_indonesian_60
        self.best_english_30 = best_english_30
        self.best_english_60 = best_english_60

    # __str__ method
    def __str__(self):
        output = ''
        output += '\nYour Information:'
        output += f'\n- Username: {self.username}'
        output += f'\n- Password: {self.password}'
        output += f'\n- Best Indonesian 30 seconds: {self.best_indonesian_30} words correct'
        output += f'\n- Best Indonesian 60 seconds: {self.best_indonesian_60} words correct'
        output += f'\n- Best English 30 seconds: {self.best_english_30} words correct'
        output += f'\n- Best English 60 seconds: {self.best_english_60} words correct'
        return output

    # save_user_to_files method
    def save_user_to_files(self):
        try:
            with open('files/user.csv', 'a') as f:
                f.write(f'{self.username},{self.password},{self.best_indonesian_30},{self.best_indonesian_60},{self.best_english_30},{self.best_english_60}\n')
        except Exception as e:
            print(f'Error: {e}')

    # load_user_from_files method
    def load_user_from_files(username):
        column_handler = 0
        try:
            with open('files/user.csv', 'r') as f:
                for line in f:
                    if column_handler == 0: # Skip header line
                        column_handler += 1
                        continue
                    line_list = line.split(',')
                    line_username = line_list[0]
                    line_password = line_list[1]
                    line_best_indonesian_30 = int(line_list[2])
                    line_best_indonesian_60 = int(line_list[3])
                    line_best_english_30 = int(line_list[4])
                    line_best_english_60 = int(line_list[5])
                    if line_username == username:
                        return User(line_username, line_password, line_best_indonesian_30, line_best_indonesian_60, line_best_english_30, line_best_english_60) # Return user object if found
        except Exception as e:
            print(f'Error: {e}')
        return None
    
    # set_best_score method
    def set_best_score(self, language, timer, score):
        if language == 'indonesian' and timer == '30':
            if score > self.best_indonesian_30:
                self.best_indonesian_30 = score
                return True
        elif language == 'indonesian' and timer == '60':
            if score > self.best_indonesian_60:
                self.best_indonesian_60 = score
                return True
        elif language == 'english' and timer == '30':
            if score > self.best_english_30:
                self.best_english_30 = score
                return True
        elif language == 'english' and timer == '60':
            if score > self.best_english_60:
                self.best_english_60 = score
                return True
        return False
    
    # update_user_in_files method
    def update_user_in_files(self):
        users = []
        column_handler = 0
        header = []
        try:
            with open('files/user.csv', 'r') as f: # Read all users
                for line in f:
                    if column_handler == 0: # Handle header line
                        header.append(line)
                        column_handler += 1
                        continue
                    line_list = line.split(',')
                    line_username = line_list[0]
                    if line_username == self.username: # Update only current user data
                        users.append(f'{self.username},{self.password},{self.best_indonesian_30},{self.best_indonesian_60},{self.best_english_30},{self.best_english_60}\n') # Update user data
                    else:
                        users.append(line) # Keep other user data
            with open('files/user.csv', 'w') as f: # Write back all users
                for header_line in header: # Write header line
                    f.write(header_line)
                for user_line in users: # Write user lines
                    f.write(user_line)
        except Exception as e:
            print(f'Error: {e}')