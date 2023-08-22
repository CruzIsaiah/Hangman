import random
import tkinter as tk
from definitions import word_definitions


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("HM Study Game")

        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        self.guessed_letters = []
        self.guessed_word = []
        self.is_playing = False

        self.create_widgets()

    def create_widgets(self):
        self.definition_label = tk.Label(
            self.root, text="", font=("Helvetica", 12))
        self.definition_label.pack()

        self.word_label = tk.Label(self.root, text="")
        self.word_label.pack()

        self.guess_label = tk.Label(self.root, text="Guess a letter: ")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.guess_button = tk.Button(
            self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

        self.guessed_letters_label = tk.Label(
            self.root, text="Guessed Letters:")
        self.guessed_letters_label.pack()

        self.guessed_letters_display = tk.Label(self.root, text="")
        self.guessed_letters_display.pack()

        self.play_again_button = tk.Button(
            self.root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.config(state='disabled')

        self.start_game()

    def start_game(self):
        self.word, self.definition = random.choice(
            list(word_definitions.items()))
        self.guessed_word = ["_"] * len(self.word)
        self.is_playing = True
        self.incorrect_guesses = 0
        self.guessed_letters = []

        self.definition_label.config(text=f"Hint: {self.definition}")
        self.update_word_to_show()
        self.guess_button.config(state='active')
        self.play_again_button.config(state='disabled')

    def check_guess(self):
        if not self.is_playing:
            return

        guess = self.guess_entry.get().lower()

        if not guess:
            self.guess_entry.delete(0, 'end')
            return

        if len(guess) != 1 or (not guess.isalpha() and guess != " " and guess != "+"):
            self.message_label.config(
                text="Invalid input. Please enter a single letter, a space, or a '+' character.")
            self.guess_entry.delete(0, 'end')
            return

        if guess in self.guessed_letters:
            self.message_label.config(
                text="You have already guessed that letter. Please guess another letter.")
            self.guess_entry.delete(0, 'end')
            return

        self.guessed_letters.append(guess)
        self.update_guessed_letters_display()

        if guess in self.word.lower():
            self.update_word_to_show(guess)
        else:
            self.incorrect_guesses += 1

        if self.incorrect_guesses == 5:
            self.message_label.config(text="Careful one guess left!!")

        if self.incorrect_guesses == self.max_incorrect_guesses:
            self.message_label.config(
                text=f"You lose! The word was {self.word}")
            self.end_game()
        elif "_" not in self.word_label.cget("text"):
            self.message_label.config(text="You win!")
            self.end_game()

        self.guess_entry.delete(0, 'end')

    def update_word_to_show(self, guess=None):
        new_word_to_show = ""
        for i in range(len(self.word)):
            if guess is not None and (self.word[i].lower() == guess or self.word[i] == " "):
                self.guessed_word[i] = self.word[i]
            new_word_to_show += self.guessed_word[i] + " "

        self.word_label.config(text=new_word_to_show)

    def update_guessed_letters_display(self):
        self.guessed_letters_display.config(
            text=", ".join(self.guessed_letters))

    def end_game(self):
        self.guess_button.config(state='disabled')
        self.play_again_button.config(state='active')
        self.is_playing = False

    def play_again(self):
        self.definition_label.config(text="")
        self.message_label.config(text="")
        self.guessed_letters_display.config(text="")
        self.play_again_button.config(state='disabled')
        self.start_game()  # Call start_game to get a new hint


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
