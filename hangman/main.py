import random

wordList = "apple grape computer linux python banana"
wordList = wordList.split(" ")

wordToGuess = random.choice(wordList)
tempWord = []

livesLeft: int = 6
gameWon: bool = False

def main():
    global guessedLetter, livesLeft
    guessed = False

    print(f"lives left: {livesLeft}")
    guessedLetter = input("Guess a letter.").strip().lower()

    for i in range(len(wordToGuess)):
        if (wordToGuess[i] == guessedLetter):
            tempWord[i] = guessedLetter
            guessed = True
            break

    if guessed == False:
        livesLeft -= 1    

    for i in tempWord:
        print(f"{i}", end = "")
    
    print()
    checkWinCon()

def initTemp():
    global tempWord

    for i in wordToGuess:
        tempWord.append("_")

def checkWinCon():
    global tempWord, wordToGuess, gameWon, livesLeft

    t = ''.join(tempWord)

    if (livesLeft < 0):
        print("You lost!")

    if (wordToGuess == t):
        print("You Won!")
        gameWon = True


if (__name__ == "__main__"):
    initTemp()

    while (gameWon == False):
        main()