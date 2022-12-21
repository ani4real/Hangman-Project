#  
#task 1
import random


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = len(self.word)*['_']
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f'Good guess! {guess} is in word')
            for pos, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[pos] = char
            self.num_letters = self.num_letters - 1

        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left!')
        
        self.list_of_guesses.append(guess)


        
    def ask_for_input(self):
        
        while True:
            guess = input('Guess a letter: ')  

            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            
            elif guess in self.list_of_guesses:
                print('Oops! You\'ve already tried that letter')
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                

h_1 = Hangman(['Apple','Mango','Banana','Strawberry','Grape'])
h_1.ask_for_input()

        
        
        
