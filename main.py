import random
import urllib.request
import json

def main():
    words = []
    wordLength = input("How long do you want the word to be? ")
    try:
        wordLength = int(wordLength)
    except ValueError:
        print("That's not a number!")
        return
    if wordLength > 15 or wordLength < 4:
        print("That's not a valid word length! Choose a value between 4 and 15")
        return
    for word in json.loads(urllib.request.urlopen("https://random-word-api.herokuapp.com/all").read().decode('utf-8')):
        if len(word) == wordLength:
            words.append(word)
    word = getWord(wordLength)
    guess = ""
    found = []
    right = []
    tries = 0
    i = 0
    while guess != word:
        tries += 1
        guess = input("Guess the word: ").lower()[0:wordLength]
        if guess == "exit":
            return
        if len(guess) < wordLength or len(guess) > wordLength:
            print(f"Please enter a word with {wordLength} letters.")
            continue
        if guess not in words:
            print("Not a valid word")
            continue
        if guess == word:
            print(f"You got it! The word was {word}. It took you {tries} {'tries' if tries > 1 else 'try'}.")
            return
        i = -1
        for letter in guess:
            i += 1
            currentLetter = word[i]
            if letter == currentLetter:
                if not (letter, i) in right:
                    right.append((letter, i))
                    continue
                continue
            elif letter in word:
                if not letter in found:
                    found.append(letter)
                    continue
                continue
        output(word = word, found = found, right = right)


def output(*, word, found = [], right = []):
    i = 0
    output = ""
    output2 = ""
    for letter in word:
        if (letter, i) in right:
            output += letter
        elif letter in found:
            output2 += letter
            output += "_"
        else:
            output += "_"
        i += 1
    output2 = "".join(random.sample(output2, len(output2)))
    print(output)
    print(f"Misplaced letters: {output2}")


def getWord(length = 5):
    return json.loads(urllib.request.urlopen(f"https://random-word-api.herokuapp.com/word?length={length}").read().decode('utf-8'))[0]


if __name__ == '__main__':
    main()