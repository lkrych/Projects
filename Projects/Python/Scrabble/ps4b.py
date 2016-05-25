from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def isValidWord2 (word, hand):
    copyhand = hand.copy() #create copy of hand dictionary
    for i in word: #iterate over letters in word
        
            if i in copyhand: #if letter is in dictionary remove letter from dictionary
                copyhand[i] = copyhand[i]-1
         
            else: #if letter is not in dictionary, return False and get outta there!
                return False
                break
            if copyhand[i] == -1: #if you don't have enough letters, return False and get out
                return False
                break
    return True
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    maxScore = 0# Create a new variable to store the maximum score seen so far (initially 0)

    bestWord = ''#Create a new variable to store the best word seen so far (initially None)  
    for word in wordList:# For each word in the wordList

        if isValidWord2(word, hand) == True:# If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            x = getWordScore(word, n)# Find out how much making that word is worth
            
            if x > maxScore: # If the score for that word is higher than your best score
                maxScore = x
                bestWord = word# Update your best score, and best word accordingly
        if bestWord == '':
            bestWord = None
    return bestWord            
    
    
                


    


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0# Keep track of the total score
    
    while calculateHandlen(hand) > 0:# As long as there are still letters left in the hand:
    
        print 'Current hand: ',
        displayHand(hand)# Display the hand
        aGuess = compChooseWord(hand,wordList,n)
        
        if aGuess == None:# If the computer can't find a word
        
          
           break # End the game (break out of the loop)

            
        else:# Otherwise (the input is not a single period):
        
            if isValidWord(aGuess, hand, wordList) == False:# If the word is not valid:
            
               print 'Invalid word, please try again.'# Reject invalid word (print a message followed by a blank line)
               print                                     
            else:# Otherwise (the word is valid):
                                
                score = score + getWordScore(aGuess, n)
                
                print  "'", str(aGuess), "'", ' earned ' , getWordScore(aGuess,n) , ' points. Total: ' ,score, 'points.' # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print 
                
                hand = updateHand(hand,aGuess)# Update the hand 
                

    
    print 'Total score: ', score, ' points.'# Game is over (user entered a '.' or ran out of letters), so tell user the total score
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    replay = False #there is probably a better way to code these, but you use these variables as switches, they indicate to your program when you can replay a hand.
    replay2 = False #this grants access to your second while loop
    while True == True:    #perpetual loop until a break
        start = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
        
        if start != 'n' and start != 'r' and start != 'e': #if the user inputs a letter that doesn't make sense
            print 'Invalid command.'
        if start == 'e':
            break
        if start == 'r' and replay == False:
            replay2 = True #if you can't replay you shouldn't go into the next loop, this is reset at the bottom
            print 'You have not played a hand yet. Please play a new hand first!'
            
        if start == 'n' or start=='r' and replay2 == False:  #cool conditional statement to grant access to gameplay
            while True == True: #endless loop
               
                    startacomp = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
                    
                    if startacomp != 'u' and startacomp != 'c': 
                        print 'Invalid command.'
                    
                    if start == 'n' and startacomp =='u':
                        replay = True
                        temphand = dealHand(HAND_SIZE)
                        playHand(temphand,wordList, HAND_SIZE)
                        break
                    if start == 'r' and startacomp =='u':
                        if replay == True:
                            playHand(temphand,wordList, HAND_SIZE) 
                        if replay == False:
                            print 'You have not played a hand yet. Please play a new hand first!'
                        break
                    if start == 'n' and startacomp =='c':
                        replay = True
                        temphand = dealHand(HAND_SIZE)
                        compPlayHand(temphand,wordList, HAND_SIZE)
                        break
                    if start == 'r' and startacomp =='c':
                        if replay == True:
                            compPlayHand(temphand,wordList, HAND_SIZE) 
                        if replay == False:
                            print 'You have not played a hand yet. Please play a new hand first!'
                        break
                    
            replay2 = False #reset access to gameplay loop
                
                   # if startacomp != 'c' or startacomp !='c':
                   #     print 'Invalid command.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


