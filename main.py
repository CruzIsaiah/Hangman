# Open the text file containing the words
with open("words.txt") as word_file:
  words = word_file.read().splitlines()

play_again = True

while play_again:
  # Choose a random word from the list of words
  import random
  word = random.choice(words)

  # Initialize the game
  incorrect_guesses = 0
  max_incorrect_guesses = 6
  guessed_letters = []

  # Loop until the player either wins or loses
  while incorrect_guesses < max_incorrect_guesses:
    # Show the word with underscores for unguessed letters
    word_to_show = ""
    for letter in word:
      if letter in guessed_letters:
        word_to_show += letter
      else:
        word_to_show += "_"
    print(word_to_show)

    # Check if the player has won
    if "_" not in word_to_show:
      print("You win!")
      break

    # Prompt the player to make a guess
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single character.")
      continue
    if guess in guessed_letters:
      print(
        "You have already guessed that letter. Please guess another letter.")
      continue
    guessed_letters.append(guess)
    if guess in word:
      # Correct guess
      continue
    else:
      # Incorrect guess
      incorrect_guesses += 1
      # Guess warning
    if incorrect_guesses == 5:
      print("Careful one guess left!!")

    # Check if the player has lost
    if incorrect_guesses == max_incorrect_guesses:
      print("You lose! The word was", word)
      break

  # Ask the user if they want to play again
  play_again_input = input("Do you want to play again (y/n)? ")
  if play_again_input.lower() != "y":
    play_again = False

print("Goodbye!")
