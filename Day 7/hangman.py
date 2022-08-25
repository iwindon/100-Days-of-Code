import random
from secrets import choice

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#print(random_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
num = len(chosen_word)
print(num)
display = []
while num > 0:
    display.append("_")
    num -= 1
guess = input("Guess a letter: ").lower()

#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#print(user_guess)
index = 0
for letter in chosen_word:
    if letter == guess:
        display[index] = guess
    index += 1

    


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# My initial version, while it works I was shown there is a way to do it with less lines of code.


# word_length = len(random_word)
# num = 0
# while num < word_length:
#     if user_guess == random_word[num]:
#         print("Correct")
#         num += 1
#     else:
#         print("Wrong")
#         num += 1

# for letter in chosen_word:
#     if letter == guess:
#         print("Correct")
#     else:
#         print("Wrong")

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)