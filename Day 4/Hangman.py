import random
word_list = ["camel","baloon","lion","mouse", "orange"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
placholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placholder += "_"
print(placholder)
correct_version = []
game_over = False
while not game_over:
    guess = input("Enter a letter:\n").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_version.append(guess)
        elif letter in correct_version:
            display+=letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("O lives left, Game Over.")
            game_over = True
    if "_" not in display:
        print("You WON!")
        game_over = True