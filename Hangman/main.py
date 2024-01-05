import os
def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\033c', end='')
import random
from Hangman import logo, stages, wordlist

print(logo.logo)
display = []
chosen_word = random.choice(wordlist.word_list)
word_lenght = len(chosen_word)
# print(f'Pssst, the solution is {chosen_word}.')
for _ in range(word_lenght):
    display += '_'
lives = 6
end_of_game = False
while not end_of_game:
    print(display)
    guess = str(input('Guess a letter: ')).strip().lower()
    clear()
    if guess in display:
        print('You have entered this letter already')
    for position in range(word_lenght):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in chosen_word:
        lives = lives - 1
        print(f'{guess} is not in the word. You lose a life.')
        print(stages.stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lose.')
    if "_" not in display:
        end_of_game = True
        print('You win.')
