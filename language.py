'''
This is language module for handling language-related processes.

This module has following functions:
- load_language: Load language data from files/language/<language>.txt and return as list for english and list of lists for indonesian (since there are same words but different translations, ex: adalah).
'''

# load_language function
def load_language(language):
    language_data = []
    try:
        with open(f'files/language/{language}.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if language == 'english':
                    language_data.append([line])  # English is a list
                else: # Indonesian
                    word_translation = line.split(' = ') # Words and translations
                    language_data.append(word_translation) # Indonesian is a list of lists [word, translation]
    except Exception as e:
        print(f'Error: {e}')
    return language_data