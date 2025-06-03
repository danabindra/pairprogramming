from scrabble_values import SCRABBLE_POINTS
import random

def get_random_letters(n=7):
    return random.choices(list(SCRABBLE_POINTS.keys()), k=n)

def score_word(word):
    return sum(SCRABBLE_POINTS.get(letter.upper(), 0) for letter in word)

def main():
    print("Welcome to Scrabble Showdown!")
    letters = get_random_letters()
    print("Your letters:", " ".join(letters))

    word = input("Enter a word using these letters: ").upper()
    valid = all(word.count(char) <= letters.count(char) for char in word)

    if valid:
        print("Your word score:", score_word(word))
    else:
        print("Invalid word. You used letters you don't have.")

if __name__ == "__main__":
    main()
