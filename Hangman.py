# Step 1
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

selected_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
length_word = len(selected_word)
for _ in range( length_word):
    display += "_"
print(display)

end_of_game = False
a = 6
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


while not end_of_game:
    guess_letter: str = (input("Guess a letter:").lower())
    for position in range(length_word):
        letter = selected_word[position]
        if letter == guess_letter:
            display[position] = letter
    print(display)


    if guess_letter not in selected_word:
        a -= 1
        if a == 0:
            end_of_game = True
            print("You Lose")

    if "_" not in display:
        end_of_game = True
        print("You Won")
        print("You won!! \nCorrect answer is: " + selected_word)
    print(stages[a])