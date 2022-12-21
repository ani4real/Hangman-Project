import random

wordlist = ['Banana', 'Apple', 'Orange', 'Strawberry','Grape']
print(wordlist)

word = random.choice(wordlist)
print(word)

while True:
    guess = input('Enter a single character')

    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        break    
    else:
        print('Oops! That is not a valid input')
    
import random

wordlist = ['Banana', 'Apple', 'Orange', 'Strawberry','Grape']
print(wordlist)

word = random.choice(wordlist)
print(word)

# task 2
while True:
    guess = input('Enter a single character')

    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        break    
    else:
        print('Invalid letter! Please enter a single character.')
        

if guess in word:
    print('Good guess! {} is in the word.'.format(guess))
else:
    print('Sorry, {} is not in the word. Try again.'.format(guess))