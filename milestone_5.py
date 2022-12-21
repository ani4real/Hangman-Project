
import random           #random module in Python defines a series of functions for generating or manipulating random integers


class Hangman:
    def __init__(self, word_list, num_lives = 5):   #Initialising in class
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)        #With the help of random module a word is ranodmly chosen from a list
        self.num_letters = len(set(self.word))      #Number of letters will be stored as sets to prevent recounting recurring letters
        self.word_guessed = len(self.word)*["_"]
        self.list_of_guesses = []
    
    def check_guess(self, guess):                   #Creating a function for checking the user input's guess
        guess = guess.lower()                       #converting the guess into a lowercase 
        
        if guess in self.word:                          #creating an if statemnt to check if the guessed letter is in the word that was randomly picked from the list
            print(f'Good guess! {guess} is in word')    
            for pos, char in enumerate(self.word):      #using the enumerate function to index the word and find the position of the guessed letter
                if char == guess:
                    self.word_guessed[pos] = char
            self.num_letters -= 1
            print(f"{self.word_guessed}")
            return self.word_guessed              
        else:
            self.num_lives -= 1                             #if the lettter guesssed is incorrected the user will lose a life in the game.
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left!')  
        
        self.list_of_guesses.append(guess)                  #the guessed letter will be added to a list so the user cannot guess the same letter once again
        print(self.list_of_guesses)
        


        
    def ask_for_input(self):                                #Function to get the input from the user
        
    
        guess = input('Guess a letter: ')  

        if not (len(guess) == 1 and guess.isalpha()):
            print('Invalid letter. Please, enter a single alphabetical character.')     #checking if the user guess is just one single letter
        
        elif guess in self.list_of_guesses:
            print('Oops! You\'ve already tried that letter')
        
        else:
            self.check_guess(guess)
                
                
def play_game(word_list, num_lives):                
    
    game = Hangman(word_list, num_lives)            #instantiating the class by creating an object called game
    
    while True:
        if game.num_lives == 0:                     #if the user keeps guessing incorrectly till the life is 0. The game ends in a loss
            print('Oh no you have lost!')
            break
        elif game.num_letters > 0:                  
            game.ask_for_input()
        else:
            print('Congrats you\'ve won!')          #conversely if the user gets all the guesses correct, the game ends in victory!!
            break
play_game(['orange', 'lemon', 'mango', 'pineapple', 'strawberry'], 5)       
