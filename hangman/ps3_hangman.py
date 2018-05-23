
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import onlinedict

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME, 'r', -1) as inFile:
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
        print ("  ", len(wordlist), "words loaded.")
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
    # FILL IN YOUR CODE HERE...
    secretWord = set(secretWord)
    lettersGuessed = set(lettersGuessed)
    if secretWord & lettersGuessed == secretWord:
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
    # FILL IN YOUR CODE HERE...
    s = ''
    for i in secretWord:
        if i in lettersGuessed:
            s += i
        else:
            s += '_ '
    return s




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    st = set(string.ascii_lowercase) - set(lettersGuessed)
    return ''.join(sorted(st))



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
    # FILL IN YOUR CODE HERE...
    print('\tWelcome to the game Hangman!')
    length_secret = len(secretWord)
    print('\tI am thinking of a word that is %d letters long' %length_secret)
    print('\t-----------')
    mistakesMade = 0
    lettersGuessed = []
    while mistakesMade < MAX_TIMES:
        print('\tYou have %d guesses left' % (MAX_TIMES - mistakesMade))
        print('\tAvailable Letters: ' + getAvailableLetters(lettersGuessed))
        letter = input('\tPlease guess a letter: ')
        while len(letter)!=1 or letter not in string.ascii_letters:
            print('\tThe character is not a letter!')
            letter = input('\tPlease guess a letter: ')
        letter = letter.lower()
        if letter in lettersGuessed:
            print("\tOops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letter.lower())
            if letter in secretWord:
                print('\tGood guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakesMade += 1
                print('\tOops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
        print('\t-----------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('\tCongratulations, you won!')
            break
    if mistakesMade >= MAX_TIMES:
        print('\tSorry, you ran out of guesses. The word was %s. ' % secretWord)
    #return 0
    try:
        dic = onlinedict.getec(secretWord)
    except:
        print('\t网络连接错误！')
    else:
        if dic['means'] != -1:
            print('\t============')
            print("\t"+secretWord+"\n\t-----------\n\t", end='')
            print('\n\t'.join(dic['means']))
            if 'shape' in dic:
                print('\t-----------')
                for k in dic['shape']:
                    print("\t"+k)
        else:
            print('\t词典中没有查到该单词！')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

MAX_TIMES = 8
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
