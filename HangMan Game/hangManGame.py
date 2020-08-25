import random, re, sys

# ASCII SPRITE FOR THE GAME
HANGMAN_PICS = [
    '''
       +---+
           |
           |
           |
          ===''',
    '''
       +---+
       O   |
           |
           |
          ===''',
    '''
       +---+
       O   |
       |   |
           |
          ===''',
    '''
       +---+
       O   |
     / |   |
           |
          ===''',
    '''
       +---+
       O   |
     / | \ |
           |
          ===''',
    '''
       +---+
       O   |
     / | \ |
      /    |
          ===''',
    '''
       +---+
       O   |
     / | \ |
      / \  |
          ===''']

def randomWordGen():
    # OPEN THE CONTAINING LISTS OF WORDS
    wordsFile = open("words.txt")

    # READING THE TEXT FILE
    words = wordsFile.read()
    # print(wordsFile.read())

    # MODIFYING THE TEXT FILE
    words = words.replace("\"","")              # Remove " from the text
    words = words.split(",")                    # Turn it into a list by comma
    index = int(random.random()* len(words))    # Generate the index of the that random word
    #print(words[index])
    return words[index]


def HANG_MAN():
    # DECLARE VARIABLE 
    word = randomWordGen()                      # Generate word to use from randomWordGen()
    tempWord = word
    hangingCount = 0                            # Count for each fail guess
    hangingCount1 = 1                           # Same use for above but is used to swap to the next image.
    blankHolder = "_" * len(word)               # Generate the blank underscores based on the word's length
    user_input = ""
    updatePic = HANGMAN_PICS[0]
    
    #print(word)

    # GAME PLAY RUNS
    while (True):
        # PRINT OUT GAME PLAY
        print(updatePic + "  " + blankHolder)
        if '_' not in blankHolder:
            print("You win!")
            sys.exit()
        
        user_input = input("Enter a letter: ")
        if len(user_input) > 1 or len(user_input) == 0:
            print("Please enter a letter")
        elif not re.match("^[a-z]*$", user_input):
            print("Please enter a letter")
        else:
            if user_input in word:
                # TEMP VARIABLE
                temp = list(blankHolder)                                # TURN THE TEMP INTO A LIST CONTAINING UNDERSCORED CHAR
                count = word.count(user_input)                          # COUNT TO LOOP FOR SPECIFIC PATTERN OF A CHARACTER

                # LOOP FOR SPECIFIC PATTERN OF A LETTER
                # THIS REPLACES THE UNDERSCORES MYSTERY WITH THE CORRECT GUESSED LETTER AT THE SPECIFIC INDEX
                # .find() return the index
                for x in range(count):
                    temp[tempWord.find(user_input)] = user_input
                    blankHolder = "".join(temp)                         # REJOIN THE LIST INTO STRING
                    tempWord = tempWord.replace(user_input,"_", 1)      # REPLACE THE TEMP FROM LETTER TO UNDERSCORE CHAR ONE BY ONE. EX: BABY -> _ABY 
                                                                                                     
                print("\nYou found the letter!")
            else:
                # PRINT THE NEXT HANGMAN IMAGE FROM HANGMAN_PICS UNTIL THE MAN IS FULLY HANG.
                # REPLACE THE PREVIOUS PIC WITH THE NEXT PIC
                updatePic = updatePic.replace(HANGMAN_PICS[hangingCount], HANGMAN_PICS[hangingCount1])
                hangingCount+= 1
                hangingCount1+= 1
                # IF WE REACH THE FINAL IMAGE, EXIT THE GAME    
                if hangingCount == len(HANGMAN_PICS) - 1:
                    print("\nYou used all your attempt!")
                    print(updatePic + "\tThe word is " + word)
                    sys.exit()
                else:
                    print("\nOh no! Take another guess")
                                               
            

HANG_MAN()




