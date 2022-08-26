from dis import dis
import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

print(logo)

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

    if guess in display:
        print(f"You already guessed the letter {guess}")


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
        print(f"The letter {guess} is not in the word.  You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])