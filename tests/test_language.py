# Library imports
import sys
import os

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Main function imports
from language import load_language

# Test: language Indonesian
def test_language_indonesian():
    expected = [['sebagai','as'],['saya','I']]
    actual = load_language('indonesian')
    assert actual == expected, 'test_language_indonesian failed: Incorrect language loading.'
    print('test_language_indonesian passed!')

# Test: language English
def test_language_english():
    expected = ['a','ability']
    actual = load_language('english')
    assert actual == expected, 'test_language_english failed: Incorrect language loading.'
    print('test_language_english passed!')

# Run all tests
if __name__ == '__main__':
    test_language_indonesian()
    test_language_english()