import random

wordlist = ['Banana', 'Apple', 'Orange', 'Strawberry','Grape']

word = random.choice(wordlist)
print(word)

#task 3


def check_guess(guess): 
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')


def ask_for_input():
    
    while True:
        guess = input('Enter a single character: ')

        if len(guess) == 1 and guess.isalpha():
            print('Good guess!')
            break    
        else:
            print('Invalid letter! Please enter a single character: ')

ask_for_input()




