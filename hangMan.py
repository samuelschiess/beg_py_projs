from getpass import getuser


gameOver = False
gameWon = False

currentGuess = ""

#picture to display variables
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
secretWord = "ounce"
secretWordLetters = ["o", "u", "n", "c", "e"]
secretWordDisplayList = ["Secret Word:", "_", "_", "_", "_", "_"]
secretWordDisplay = " ".join(secretWordDisplayList)

#wrong guess variables
wrongGuessedLetters = ["wrong letters:"]
wrongGuessedWords = ["wrong words:"]

def wrongLetter():
    global currentGuess
    global wrongGuessedLetters
    wrongGuessedLetters += currentGuess

def wrongWord():
    global currentGuess
    global wrongGuessedWords
    wrongGuessedWords += currentGuess

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
    global gameOver 
    gameOver = True



#compile the above functions into a list and call the correct one at anytime with wrongGuess function
sixChances = [wrongGuess1, wrongGuess2, wrongGuess3, wrongGuess4, wrongGuess5, wrongGuess6]
currentChanceIndex = 0

def wrongGuess():
    global currentChanceIndex
    sixChances[currentChanceIndex]()
    currentChanceIndex += 1

#function to hange "secret word display" 
def correctGuess():
    indexToChange = secretWordLetters.index(currentGuess) + 1
    global secretWordDisplayList 
    secretWordDisplayList[indexToChange] = currentGuess
    global secretWordDisplay
    secretWordDisplay = " ".join(secretWordDisplayList)
    global gameWon
    if "_" not in secretWordDisplayList:
        gameWon = True


#display the wrong guesses
def showWrongGuesses():
    print(" ".join(wrongGuessedLetters))
    print(" ".join(wrongGuessedWords))

#the next two functions are part of the later getUserGuess function
def checkCurrentGuessWord():
    global gameWon
    if currentGuess == secretWord:
        gameWon = True
    else:
        wrongGuess() #changes the picture display and ends game if complete
        wrongWord() #adds to the wrong word list
    
def checkCurrentGuessLetter():
    if currentGuess in secretWordLetters:
        correctGuess()

    else:
        wrongGuess() #changes the picture display and ends game if complete
        wrongLetter() #adds to the wrong letter list

def getUserGuess():
    global currentGuess
    currentGuess = input("Guess a five-letter lower case word or letter, no spaces: ")
    if len(currentGuess) == 5:
        checkCurrentGuessWord() 
    elif len(currentGuess) == 1:
        checkCurrentGuessLetter()
    else:
        print("wrong word length")


#GAME LOOP
while True:
    print("")
    showWrongGuesses()
    printPicture()
    print(secretWordDisplay)
    if gameOver == True:
        print("You Suck at This!!!!!")
        print()
        print("GAME OVER")
        break
    if gameWon == True:
        print("Incredible!!!! You got the right word!")
        print()
        print("YOU WIN")
        break
    getUserGuess()
    

