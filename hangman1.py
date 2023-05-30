import random

already_guessed = 0
correct = 1
wrong = 2

def get_random_word(wordfile = "/usr/share/dict/words"):
    candidate_words = []
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word

def masked_word(word, guess):
    guess_word = []
    for i in word:
        if i in guess:
            guess_word.append(i)
        else:
            guess_word.append('-')
    return "".join(guess_word)        

def get_status(secret_word, guesses, turns_remaining):
    mask_word = masked_word(secret_word, guesses)
    guessed_letters = " ".join(guesses)
    return f"""Secret word:{mask_word}
Guesses : {guessed_letters}
Remaining turns : {turns_remaining}"""

def check(secret_word, guesses, turns_remaining, new_guess):    
    if new_guess in guesses:
        return already_guessed, turns_remaining
    else:
        guesses.append(new_guess)
        if new_guess in secret_word:
            return correct, turns_remaining
        else:
            return wrong, turns_remaining-1

def game_over(secret_word, guesses, turns_remaining):
    if turns_remaining == 0:
        return True, f"You lost! The word was {secret_word}"
    masked = masked_word(secret_word, guesses)
    if "-" in masked:
        return False, None
    else:
        return True, f"You guessed it! The word was {secret_word}"


# def main():
#     secret_word = get_random_word()
#     print (secret_word)
#     guesses = []
#     turns_remaining = 8
#     while True:
#         print (get_status(secret_word, guesses, turns_remaining))
#         guess = input("Enter a letter ")
        
#         status, turns_remaining = check(secret_word, guesses, turns_remaining, guess)
#         if status == already_guessed:
#             print ("You already guessed that")
        
#         finished, message = game_over(secret_word, guesses, turns_remaining)
#         if message:
#             print (message)
#         if finished:
#             break


# if __name__ == "__main__":
#     main()