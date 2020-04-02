#importing the file so that I can get the words
import get_word

#Declaring varibles 
lives = 5
letters_guessed = []
underscores = []

#printing the header
print( "\n \n \n \n \n \n \n")
print ("+++++++++++++++===================Welcome to Hangman+++++++++++++++===================")
print( "\n \n")

#getting the word from the other file
word = get_word.get_word().lower()

#filling the underscores list with the amount of underscores in the word
for x in word:
    underscores.append("_") 

while lives > 0:

    print (" ".join(underscores))
    print ("you have",lives,"lives left")
    letter = input("enter the letter that you want to guess: ")
    
    if(letter == word):
        print ("you should try a higher difficutly")
        break

    elif letter in letters_guessed or len(letter)>1:
    
        print ("invaild move")
    
    elif letter in word:
    
        letters_guessed.append(letter)
    
        for x in range (len(word)):
    
            if word[x] == letter:
    
                underscores[x] = letter
    
    elif letter not in word:
    
        letters_guessed.append(letter)
        lives -= 1
        print ("the letter you guessed isn't in the word")
    
    if "_" not in underscores:
    
        print("Good Job!")
        break


if "_" in underscores:
    print("Game over! The correct word was", word)
