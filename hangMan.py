gameOver = False

currentGuess = ""

#picture to display
displayLine1 = "----------"
displayLine2 = "|        |"
displayLine3 = "|"
displayLine4 = "|"
displayLine5 = "|"
displayLine6 = "|"
displayLine7 = "|"
displayLine8 = "|"
displayLine9 = "|"
displayLine10 = "____________________"

#secret word variables
secretWord = "penis"
secretWordLetters = ["p", "e", "n", "i", "s"]
secretWordDisplayList = ["Secret Word: ", "_", "_", "_", "_", "_"]
secretWordDisplay = " ".join(secretWordDisplayList)

#wrong guess variables
wrongGuessedLetters = ["wrong letters: "]
wrongGuessedWords = ["wrong words: "]


def printPicture():
    print(displayLine1) 
    print(displayLine2) 
    print(displayLine3) 
    print(displayLine4) 
    print(displayLine5) 
    print(displayLine6) 
    print(displayLine7) 
    print(displayLine8) 
    print(displayLine9) 
    print(displayLine10) 

#Functions to change the picture after each wrong guess
def wrongGuess1():
    global displayLine3 
    displayLine3 = "|        0"

def wrongGuess2():
    global displayLine4
    displayLine4 = "|        | "
    global displayLine5
    displayLine5 = "|        | "

def wrongGuess3():
    global displayLine4
    displayLine4 = "|       /|"
    global displayLine5
    displayLine5 = "|      / |"

def wrongGuess4():
    global displayLine4
    displayLine4 = "|       /|\ "
    global displayLine5
    displayLine5 = "|      / | \ "

def wrongGuess5():
    global displayLine6
    displayLine6 = "|       / "
    global displayLine7
    displayLine7 = "|      /   "

def wrongGuess6():
    global displayLine6
    displayLine6 = "|       / \  "
    global displayLine7
    displayLine7 = "|      /   \ "

#Change secret word disply variable
def correctGuess(guessLetter):
    indexToChange = secretWordLetters.index(guessLetter)
    global secretWordDisplayList 
    secretWordDisplayList[indexToChange] = guessLetter
    global secretWordDisplay
    secretWordDisplay = " ".join(secretWordDisplayList)

def showWrongGuesses():
    print(wrongGuessedLetters)
    print(wrongGuessedWords)
    
def userGuesses():
    global currentGuess
    currentGuess = input("Guess a five-letter lower case word or letter, no spaces: ")
    if len(currentGuess) == 5:
        print("it's a word") 
    elif len(currentGuess) == 1:
        print("it's a letter")
    else:
        print("wrong word length")

def checkCurrentGuessWord():
    if currentGuess == secretWord:
        print("You Win!!!")
    
def checkCurrentGuessLetter():
    if currentGuess in secretWordLetters:
        print("That is a correct letter!!!")

userGuesses()
checkCurrentGuessLetter()