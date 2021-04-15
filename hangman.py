# Michelle Co 195705 
# Nirel Ibarra, 192468
# April 13, 2021

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor, my/our groupmates, the teaching assistants,
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

import random, time

#categories
fruits = ['santol', 'guyabano', 'atis', 'jackfruit', 'pineapple','lemon', 'grapefruit','banana','papaya','strawberry','avocado','apricot']
superHeroes = ['wanda', 'antman', 'wasp', 'mystique', 'supergirl', 'arrow', 'vision', 'daredevil', 'thor','aquaman','wanda','hulk','loki','falcon']
colors = ['blue', 'yellow', 'red', 'black', 'grey','pink','white','orange','green','violet','purple','indigo','gold','silver']
characters = ['meredith','lexie','ross','derek','maggie','rachel','monica','joey','amy','jake']
songs = ['afterglow','red','lover','roses','easily','positions','fallig','wap','mirrorball']
names = ['michelle','nirel','gaby','samantha','kirsten','cedric','joan','joyce','sofia','andrea','angelina','justine','james','kristelle','geanine','aurielle','patricia','alyssa','aleeza','john','lance']
animals = ['dog','cat','pig','cow','chicken','monkey','elephant','ant','bee','giraffe','lion','tiger','zebra']
planet = ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']

#use this list to determine blanks and revelaled letters
userGuesslist = []

#keeps track of the list of letters used and then compared with smallList to check letters whether or not the letters are used
userGuesses = []

#keeps track of game state
playGame = True

#to show remaining letters left
unusedSmallLetters = 'abcdefghijklmnopqrstuvwxyz'

#to show remaining letters left with mutated list
newLetters = 'abcdefghijklmnopqrstuvwxyz'

#convert unused letters to a list, then compared with userGuesses to check whether or not the letters are used
smallList = list(unusedSmallLetters)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def toString():
    for n in userGuesslist:
        print(n, end=' ')

def conversionToLowerCase(alphabet):
    if 'A' <= alphabet <= 'Z':
        if alphabet == 'A':
            alphabet = 'a'
            return alphabet
        elif alphabet == 'B':
            alphabet = 'b'
            return alphabet
        elif alphabet == 'C':
            alphabet = 'c'
            return alphabet
        elif alphabet == 'D':
            alphabet = 'd'
            return alphabet
        elif alphabet == 'E':
            alphabet = 'e'
            return alphabet
        elif alphabet =='F':
            alphabet = 'f'
            return alphabet
        elif alphabet == 'G':
            alphabet = 'g'
            return alphabet
        elif alphabet == 'H':
            alphabet = 'h'
            return alphabet
        elif alphabet == 'I':
            alphabet = 'i'
            return alphabet
        elif alphabet == 'J':
            alphabet = 'j'
            return alphabet
        elif alphabet == 'K':
            alphabet = 'k'
            return alphabet
        elif alphabet == 'L':
            alphabet = 'l'
            return alphabet
        elif alphabet == 'M':
            alphabet = 'm'
            return alphabet
        elif alphabet == 'N':
            alphabet = 'n'
            return alphabet
        elif alphabet == 'O':
            alphabet = 'o'
            return alphabet
        elif alphabet == 'P':
            alphabet = 'p'
            return alphabet
        elif alphabet == 'Q':
            alphabet = 'q'
            return alphabet
        elif alphabet == 'R':
            alphabet = 'r'
            return alphabet
        elif alphabet == 'S':
            alphabet = 's'
            return alphabet
        elif alphabet == 'T':
            alphabet = 't'
            return alphabet
        elif alphabet == 'U':
            alphabet = 'u'
            return alphabet
        elif alphabet == 'V':
            alphabet = 'v'
            return alphabet
        elif alphabet == 'W':
            alphabet = 'w'
            return alphabet
        elif alphabet =='X':
            alphabet = 'x'
            return alphabet
        elif alphabet == 'Y':
            alphabet = 'y'
            return alphabet
        elif alphabet == 'Z':
            alphabet = 'z'
            return alphabet
    elif "a" <= alphabet <= "z":
        return alphabet

def blanks(n):
    stringGuessList = ''
    for n in userGuesslist:
        stringGuessList += n
    return stringGuessList

def printGuessedLetter():
    global attempts
    if attempts == 1:
        print(f"{bcolors.WARNING}Guess the word", attempts, f"guess(es) left! {bcolors.ENDC}" + blanks(userGuesslist))
    else:
        print(f"Guess the word, {attempts} guesses left: " + blanks(userGuesslist))

def notInList(smallList, userGuesses):
    newLetterList = ''
    for i in smallList:
        if not i in userGuesses:
            newLetterList += i
    return newLetterList

def checkValidity():
    global attempts
    if len(letter) != 1:
        print(f'\n{bcolors.WARNING}Please enter one letter at a time only.{bcolors.ENDC}')

    elif conversionToLowerCase(letter) in userGuesses:
        print(f"\n{bcolors.WARNING}You already guessed this letter, try something else.{bcolors.ENDC}")

    elif conversionToLowerCase(letter) not in smallList:
        print(f'\n{bcolors.WARNING}Invalid character. Please enter a letter.{bcolors.ENDC}')
    
    elif letter == "1":
        print('You asked for a hint!')
            
    else:
        userGuesses.append(conversionToLowerCase(letter))

        if conversionToLowerCase(letter) in secretWordList:
            print(f"{bcolors.OKBLUE}\nCorrect letter!{bcolors.ENDC}")
            for i in range(len(secretWordList)):
                if conversionToLowerCase(letter) == secretWordList[i]:
                    userGuesslist[i] = conversionToLowerCase(letter)

        else:
            attempts -= 1
            print("\nWrong letter. Try again.")

print("\n")
print("""$$\                 $$\  $$\                $$$$$$$\  $$\                           $$\   $$\                                                                 $$\ 
$$ |                $$ | $  |               $$  __$$\ $$ |                          $$ |  $$ |                                                                $$ |
$$ |      $$$$$$\ $$$$$$\\_/ $$$$$$$\       $$ |  $$ |$$ | $$$$$$\  $$\   $$\       $$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  $$ |
$$ |     $$  __$$\\_$$  _|  $$  _____|      $$$$$$$  |$$ | \____$$\ $$ |  $$ |      $$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ $$ |
$$ |     $$$$$$$$ | $$ |    \$$$$$$\        $$  ____/ $$ | $$$$$$$ |$$ |  $$ |      $$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |\__|
$$ |     $$   ____| $$ |$$\  \____$$\       $$ |      $$ |$$  __$$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |    
$$$$$$$$\\$$$$$$$\  \$$$$  |$$$$$$$  |      $$ |      $$ |\$$$$$$$ |\$$$$$$$ |      $$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |$$\ 
\________|\_______|  \____/ \_______/       \__|      \__| \_______| \____$$ |      \__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|\__|
                                                                    $$\   $$ |                                    $$\   $$ |                                      
                                                                    \$$$$$$  |                                    \$$$$$$  |                                      
                                                                     \______/                                      \______/                                        """)
time.sleep(1)                                                                     
print("Welcome to Hangman!")
time.sleep(1)
print("The objective of the game is to guess the word before you run out of guesses.")
time.sleep(1)
print("Be sure to enter one letter at a time only. Press enter to see if you guessed correctly")
time.sleep(1.5)
print("Hope you have fun!")
time.sleep(1)

while True:
    #User prompt to ask wether or not the game will use a random word
    setWord = input('Would you like a random word? Press "y" or "n" ')

    #random word is given
    if conversionToLowerCase(setWord) == 'y':
        #Choosing the category of the random word
        print('Please select a valid category:\n"f" for fruits,\n"sh" for superheroes,\n"c" for colors,\n"ch" for characters,\n"s" for songs,\n"n" for names,\n"a" for animals,\n"p" for planets,\n"b" to go back ')

        category = input()
        if conversionToLowerCase(category) == 'sh':
            secretWord = random.choice(superHeroes)[0:]

        elif conversionToLowerCase(category) == 'f':
            secretWord = random.choice(fruits)[0:]
        
        elif conversionToLowerCase(category) == 'c':
            secretWord = random.choice(colors)[0:]
        
        elif conversionToLowerCase(category) == 'ch':
            secretWord = random.choice(characters)[0:]

        elif conversionToLowerCase(category) == 's':
            secretWord = random.choice(songs)[0:]
        
        elif conversionToLowerCase(category) == 'n':
            secretWord = random.choice(names)[0:]

        elif conversionToLowerCase(category) == 'a':
            secretWord = random.choice(animals)[0:]

        elif conversionToLowerCase(category) == 'p':
            secretWord = random.choice(planet)[0:]

        elif conversionToLowerCase(category) == 'b':
            continue

    #user selects the word to be guessed
    elif conversionToLowerCase(setWord) == 'n':
        secretWord = input('Please enter word to be guessed here: ')
        conversionToLowerCase(secretWord)
    
    else:
        print(f'{bcolors.WARNING}\nYou did not press the correct key. Please try again.\n{bcolors.ENDC}')
        continue

    if playGame:
        print('The word to be guessed is: ' + secretWord)
        secretWordList = list(secretWord)
        setAttempts = input('Would you like to set number of guesses? Press "y" or "n", "b" to go back ')

        if conversionToLowerCase(setAttempts) == 'y':
            attempts = int(input('How many guesses? '))

        elif conversionToLowerCase(setAttempts) == 'n':
            attempts = (len(secretWord) + 2)
        
        elif conversionToLowerCase(setAttempts) == 'b':
            continue

        #Adding blank lines to userGuesslist to create the blank secret word
        for n in secretWordList:
            userGuesslist.append('-')

        #Game starts here
        while True:
            printGuessedLetter()
            print("Unused letters: ", notInList(smallList, userGuesses))
            letter = input()
            conversionToLowerCase(letter)
            checkValidity()

            #test values

            # print(userGuesslist)
            #compared with blanks
            #output: ['r', 'a', 'n', 'd', '-', '-']

            # print(secretWordList)
            #the secret word converted into a list
            #output: ['r', 'a', 'n', 'd', 'o', 'm']

            # print(userGuesses)
            #all of the guesses are listed here whether or not they are correct
            #output: ['r', 'a', 'n', 'd', 'o', 'm']

            #Win/loss logic for the game
            if userGuesslist == secretWordList:
                print("\nCONGRATULATIONS! YOU WIN")
                break
            elif attempts == 0:
                print(f"{bcolors.FAIL}YOU LOSE! {bcolors.ENDC}")
                print("The secret word was: "+ secretWord)
                break

        #Play again logic for the game
        continueGame = input(f"{bcolors.BOLD}Do you want to play again? Y to continue, any other key to quit: {bcolors.ENDC}")
        if conversionToLowerCase(continueGame) == 'y':
            playGame = True
            userGuesslist = []
            userGuesses = []
            category = ""
            setWord = ""
            setWord = "Y"
            continueGame = "Y"
        else:
            print('\n')
            print('Thank you for playing!\n')
            time.sleep(1)
            print("""/$$$$$$$                      /$$
| $$__  $$                    | $$
| $$  \ $$ /$$   /$$  /$$$$$$ | $$
| $$$$$$$ | $$  | $$ /$$__  $$| $$
| $$__  $$| $$  | $$| $$$$$$$$|__/
| $$  \ $$| $$  | $$| $$_____/    
| $$$$$$$/|  $$$$$$$|  $$$$$$$ /$$
|_______/  \____  $$ \_______/|__/
           /$$  | $$              
          |  $$$$$$/              
           \______/               \n""")
            break
    else:
        break