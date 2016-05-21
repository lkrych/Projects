# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open("words.txt" , 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guess = [] #creates an empty list for storage
    for i in secretWord: #loops through secretWord to see if the user guessed the letters of the word 
        if i in lettersGuessed: #compares each letter to the list of letters in 'letters guessed
            guess.append(i)
    if len(guess) == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = '' #creates an empty string for storage
    for i in secretWord: #loops through secretWord to see if the user guessed the letters of the word 
        if i in lettersGuessed: #compares each letter to the list of letters in 'letters guessed
            guess = guess + ' ' +  i + ' ' #adds letter in secret word to guess, has spaces in it so that the output is easy to read!
        else:
            guess = guess + ' _ ' #add an underspace if the user does not guess the right letter!
    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    guess = '' #creates an empty string for storage
    for i in (alpha): #loops through secretWord to see if the user guessed the letters of the word 
        if i in lettersGuessed: #compares each letter to the list of letters in 'letters guessed
            0 #space... not sure what the best way to do this is..       
        else:
            guess = guess + i #add an underspace if the user does not guess the right letter!
    return guess
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = [] #create an empty list
    
    count = 8 #the intializing factor of your decrementing function
    
    print 'Welcome to the game, Hangman!' 
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.' #let the user know how many letters are in the word
    print '-----------'
    while count >= 1: #the while loop, trusty friend... counts down until 1
        print 'You have ' + str( count )+ ' guesses left.' #designed to print your count list
        print 'Available letters: ' + getAvailableLetters(lettersGuessed) #access your function getAvailableLetters, this prints out all letters that haven't been guessed
        count-=1 
        aGuess = raw_input('Please guess a letter: ').lower() #let your user input a letter and converts capital letters to lowercase
        if aGuess in lettersGuessed:
            print 'Oops! You\'' + 've already guessed that letter: ' + getGuessedWord(secretWord,lettersGuessed) 
            count+=1 #if you repeat your guess, don't decrement the counts
        else:
            lettersGuessed.append(aGuess) #add guess to list!
            if aGuess in secretWord:
                count+=1 #if you guess the right letter, don't decrement the counts
                print 'Good guess: '+ getGuessedWord(secretWord,lettersGuessed)
            else:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord,lettersGuessed)
        print '-----------'
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print 'Congratulations, you won!'
            break
        if count < 1: #make sure you don't give them too many guesses!
            print 'Sorry, you ran out of guesses. The word was '+ (secretWord) +  '.'
            print     '________' 
            print     '|'' '' '' '' '' '' '' ' '|'
            print     '|'' '' '' '' '' '' '' ' 'O'
            print     '|'' '' '' '' '' '' '' ' '|'
            print     '|'' '' '' '' '' '' '' ' '^'
            print     '|'
            print  '-------'
            break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
