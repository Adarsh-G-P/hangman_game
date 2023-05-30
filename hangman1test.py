import os
import tempfile

import hangman1

def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman1.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","policeman\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman1.get_random_word(name)
        assert secret_word == "policeman"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","pelican\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman1.get_random_word(name)
        assert secret_word == "pelican"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman1.get_random_word())
    assert len(secret_words) == 10
    
# def test_masked_word_no_guesses():
#     word = "elephant"
#     assert hangman1.masked_word(word, []) == '--------'


# def test_masked_word_wrong_guesses():
#     word = "elephant"
#     assert hangman1.masked_word(word, ['x']) == '--------'

# def test_masked_word_repeated_guesses():
#     word = "elephant"
#     assert hangman1.masked_word(word, ['s', 's']) == '--------'
    
# def test_masked_word_correct_guesses():
#     word = "elephant"
#     assert hangman1.masked_word(word, ['e', 'l', 'p', 'h', 'a', 'n', 't']) == 'elephant'
      
# def test_masked_word_repeated_letters():
#     word = "elephant"
#     assert hangman1.masked_word(word, ['e']) == 'e-e-----'

 

# def test_get_status_basic():
#     secret_word = "helicopter"
#     guesses = ["c", "o", "x"]
#     turns_remaining = 3
#     ret = hangman.get_status(secret_word, guesses, turns_remaining)
#     assert ret == """Secret word:----co----
# Guesses : c o x
# Remaining turns : 3"""
        
# def test_get_status_no_guesses():
#     secret_word = "helicopter"
#     guesses = []
#     turns_remaining = 8
#     ret = hangman.get_status(secret_word, guesses, turns_remaining)
#     assert ret == """Secret word:----------
# Guesses : 
# Remaining turns : 8"""


# def test_check_already_guessed():
#     secret_word = "hospital"
#     guesses = ["i", "t"]
#     turns_remaining = 5
#     new_guess = "t"
#     status, turns_remaining = hangman.check(secret_word, guesses, turns_remaining, new_guess)
#     assert status == hangman.already_guessed
#     assert turns_remaining == 5
#     assert guesses == ["i", "t"]


# def test_check_correct():
#     secret_word = "hospital"
#     guesses = ["i", "t"]
#     turns_remaining = 6
#     new_guess = "p"
#     status, turns_remaining = hangman.check(secret_word, guesses, turns_remaining, new_guess)
#     assert status == hangman.correct
#     assert turns_remaining == 6
#     assert guesses == ["i", "t", "p"]



# def test_check_wrong():
#     secret_word = "hospital"
#     guesses = ["i", "t", "p"]
#     turns_remaining = 6
#     new_guess = "x"
#     status, turns_remaining = hangman.check(secret_word, guesses, turns_remaining, new_guess)
#     assert status == hangman.wrong
#     assert turns_remaining == 5
#     assert guesses == ["i", "t", "p", "x"]

# def test_game_over_not_over():
#     secret_word = "policeman"
#     guesses = ["x", "t"]
#     turns_remaining = 5
#     finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
#     assert not finished
#     assert message == None  

# def test_game_over_over_won():
#     secret_word = "elephant"
#     guesses = ["e", "l", "p", "h", "a", "n", "t"]
#     turns_remaining = 5
#     finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
#     assert finished
#     assert message == "You guessed it! The word was elephant"


# def test_game_over_over_lost():
#     secret_word = "elephant"
#     guesses =["e", "l", "p", "h", "a", "n", "t"]
#     turns_remaining = 0
#     finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
#     assert finished
#     assert message == "You lost! The word was elephant"    
