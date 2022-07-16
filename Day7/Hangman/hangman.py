from hangman_art import logo,stages
from hangman_words import word_list
from replit import clear

print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)
display = []
lives = 6
end_of_game = False
for _ in range(len(chosen_word)):
        display += "_"
#print(display)
while not end_of_game:
        guess = input("Guess a letter: ").lower()
        clear()
        if guess in display:
                print(f"You have already typed {guess}.")
        for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                        display[position] = letter
        #print(display)
        if guess not in chosen_word:
                print(f"You entered {guess}. It's not in the word.")
                lives -= 1
                if lives == 0:
                        end_of_game = True
                        print("You lose")
                        print(f"Word was: {chosen_word}")
        if "_" not in display:
                end_of_game = True
                print("You win")
        print(f"{' '.join(display)}")
        print(stages[lives])
