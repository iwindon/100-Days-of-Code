import random
import sys
sys.path.append('/Users/ivanwindon/Documents/Code/100-Days-of-Code/Day 7')
import hangman_art

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

num = len(chosen_word)
display = []
while num > 0:
    display.append("_")
    num -= 1

# for _ in range(len(chosen_word)):
#     display += "_"
print(f"{' '.join(display)}")


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = guess
        # else:
        #     if guess not in chosen_word:
        #         print(stages[lives])
        #         print(lives)
        #         lives = lives - 1
        #         print(lives)

        index += 1

    # for position in range(len(chosen_word)):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #             display[position] = letter
    #         else:
    #             print(stages[lives])
    #             lives -= 1
            

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

    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])