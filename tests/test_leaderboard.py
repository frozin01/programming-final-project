# Library imports
import sys
import os

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Main function imports
from leaderboard import sort_leaderboard, load_leaderboard

# Test: sort_leaderboard
def test_sort_leaderboard():
    input_data = [
        {'username': 'user1', 'words_correct': 5},
        {'username': 'user2', 'words_correct': 10},
        {'username': 'user3', 'words_correct': 7}
    ]
    expected = [
        {'username': 'user2', 'words_correct': 10},
        {'username': 'user3', 'words_correct': 7},
        {'username': 'user1', 'words_correct': 5}
    ]
    actual = sort_leaderboard(input_data)
    assert actual == expected, 'test_sort_leaderboard failed: Incorrect sorting.'
    print('test_sort_leaderboard passed!')

# Test: load_leaderboard
def test_load_leaderboard():
    expected = [
        {'username': 'rozin', 'words_correct': 14}
    ]
    actual = load_leaderboard('indonesian', '30')
    assert actual == expected, 'test_load_leaderboard failed: Incorrect loading.'
    print('test_load_leaderboard passed!')

# Run all tests
if __name__ == '__main__':
    test_sort_leaderboard()
    test_load_leaderboard()