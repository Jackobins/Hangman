import random

# global variables needed for the game
dictionary = ["BANANA", "LACKADAISICAL", "IMPOSSIBLE", "GORILLA", "MONKEY"
              "BURGER", "MILKSHAKE", "ONOMATOPOEIA", "EMERGENCY", "MIDNIGHT",
              "ACACIA", "ALARM", "DRAINAGE", "SMARTPHONE", "COMMUNISM",
              "SHREK", "VEHICLE"]
count = 7
secretWord = random.choice(dictionary)
userGuesses = []


# gets a guess letter from the player, if it is wrong, the player loses a life
def getUserGuess():
    global count
    guess = input("Enter a guess: ").upper()
    while len(guess) != 1 or not guess.isalpha() or guess in userGuesses:
        print("Your guess is not valid.")
        guess = input("Enter a guess: ").upper()
    if guess not in secretWord:
        count -= 1
    return guess


# displays the number of guesses the player has left
def displayLivesLeft():
    global count
    print("You have", count, "lives left.")


def displayUserGuesses():
    print("\nYou have guessed:", userGuesses)


# displays the secret word with "_" for letters that have not been guessed
def displaySecretWord():
    for letter in secretWord:
        if letter in userGuesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")


# displays the state of the game after every guess
def displayGameBoard():
    displaySecretWord()
    displayUserGuesses()
    displayLivesLeft()


def gameIsWon():
    gameWon = True
    for letter in secretWord:
        if letter not in userGuesses:
            gameWon = False
    if gameWon:
        return True


# the game is lost if the player loses all the lives without guessing the word
def gameIsLost():
    if count <= 0:
        return True
    else:
        return False


def gameIsOver():
    return gameIsWon() or gameIsLost()


# displays the game over screen when the game is either won or lost
def displayGameOver():
    if gameIsWon():
        print("Congratulations, you won! The secret word was:", secretWord)
    elif gameIsLost():
        print("Oh no, you lost. The secret word was:", secretWord)


# plays a round of Hangman
def playOneRound():
    while not gameIsOver():
        displayGameBoard()
        userGuesses.append(getUserGuess())
    displayGameOver()


playOneRound()
