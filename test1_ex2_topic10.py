"""
ЗАДАНИЕ 1

Классы эквивалентности
Позитивные:
           Аргумент = строковому типу данных
           Аргумент = целочисленному типу данных
           Аргумент = палиндром
Негативные:
           Аргумент не может быть отрицательным целочисленным.
"""
import pytest
# from function import palindrome

@pytest.mark.parametrize("word, expected", [('kozvck', False), (123321, True), (-123, False), ('lol', True)])
def test_palindrome(word, expected):
    assert palindrome(word) == expected

def palindrome(word):
    expected = True

    if isinstance(word, str) == True:
        expected = True
    else:
        expected = False

    if isinstance(word, int) == True:
        expected = True
        if word >= 0:
            expected = True
            word = str(word)
        else:
            return False
    else:
        expected = False

    reverse_word = word[::-1]
    if word == reverse_word:
        expected = True
    else:
        expected = False

    return expected
