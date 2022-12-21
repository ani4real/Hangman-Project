
import random


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = len(self.word)*["_"]
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f'Good guess! {guess} is in word')
            for pos, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[pos] = char
            self.num_letters -= 1
            print(f"{self.word_guessed}")
            return self.word_guessed              
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left!')
        
        self.list_of_guesses.append(guess)
        print(self.list_of_guesses)
        


        
    def ask_for_input(self):
        
    
        guess = input('Guess a letter: ')  

        if not (len(guess) == 1 and guess.isalpha()):
            print('Invalid letter. Please, enter a single alphabetical character.')
        
        elif guess in self.list_of_guesses:
            print('Oops! You\'ve already tried that letter')
        
        else:
            self.check_guess(guess)
                
                
def play_game(word_list, num_lives):
    
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print('Oh no you have lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congrats you\'ve won!')
            break
play_game(['orange', 'lemon', 'mango', 'pineapple', 'strawberry'], 5)
