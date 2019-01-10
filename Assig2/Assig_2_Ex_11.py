"""
Karl Michel Koerich , 1631968
420-LCU Computer Programming , Section 2
Wednesday , October 04
R. Vincent , instructor
Assignment 2
"""

#Hangman game

#Helper code
#----------------------------------------------

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    letters = list(secretWord)

    for i in range(len(letters)):
        
        if not letters[i] in lettersGuessed:
            
            letters[i] = '_'

    return ' '.join(letters)

#----------------------------------------------
#End of helper code

def isWordGuessed(secretWord, lettersGuessed):
    """
    This function returns True if the word is correctly guessed.
    Otherwise, it returns False.
    """

    countToLength = 0
    for letter in secretWord:
        if letter in lettersGuessed:
        	countToLength += 1

    if countToLength == len(secretWord):
        return True
    else:    
    	return False

def getAvailableLetters(lettersGuessed):
    """
    This function retuns the letters that are still valid for the user to choose.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for letter in alphabet:

        if letter not in lettersGuessed:

            result += letter
            
    return result

def playAgain():

    inputUser = ''

    while inputUser != 'y' and inputUser != 'n':

        inputUser = input('Do you want to play again? \'y\' for Yes and \'n\' for No: ')
        inputUser = inputUser.lower()

    if inputUser == 'y':
        return True
    else:
        return False

def hangman(secretWord):
    """
    Function where the game actually happens, it retuns different messages
    depending on whether the user guessed the word or not.
    """
    print('\nI am thinking of a word that is', len(secretWord), 'letters long.\n')

    remainingGuesses = 8 #Initial number of guesses.
    letterInput = '1' #Arbitrary value that will not be found in getAvaiableLetters.
    lettersGuessed = [] #List of letters that the user will try.

    while (remainingGuesses != 0):

        print('You have', remainingGuesses, 'guesses left.')

        while letterInput not in getAvailableLetters(lettersGuessed) or letterInput == '': #Test for proper input

            print('Available letters: ', getAvailableLetters(lettersGuessed))
            letterInput = input('Please guess a letter: ')
            letterInput = letterInput.lower()
            if letterInput in lettersGuessed:
                print('You already guessed that letter, try again.')

        lettersGuessed.append(letterInput)

        if letterInput in secretWord:

            #Print the secretWord with the letters you already found
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed), '\n')
            winner = isWordGuessed(secretWord, lettersGuessed)
        
            if winner is True: 

                return 'Congratulations, you won!\n'
                      
        else:
            #Print the secretWord with the letters you already found
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed), '\n')
            remainingGuesses -= 1 #Decrease by 1 the guesses remaining.

    return 'Sorry, you ran out of guesses. The word was \'' + secretWord + '\'.\n'

print('Loading word list from file...')
wordlist = loadWords()
print('  ', len(wordlist), 'words loaded.\n')
print('Welcome to the game Hangman!')

while True:

    secretWord = chooseWord(wordlist).lower() #secretWord is a string in lower case.
    print(hangman(secretWord)) #The game receiving secretWord.

    if not playAgain():

        print('\nThanks for playing the game Hangman!')
        break


