import random
import hangman_stages
import word_file
lives = 6
chosen_word = random.choice(word_file.words)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("guess a letter:\n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    print(hangman_stages.stages[lives])
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOSE !!\n")
    if '_' not in display:
        game_over = True
        print("YOU WIN !!\n")

