import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess The Number")
        self.master.configure(bg='#0000ff')  # Set background color to blue
        
        self.secret_number = random.randint(1, 10)
        self.guesses_remaining = 3

        self.label = tk.Label(master, text="Guess a number between 1 and 10:", bg='#0000ff', fg='white')  # Set background color to blue
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Submit", command=self.check_guess, bg='#008080', fg='white', font=('Arial', 12, 'bold'))  # Customizing button
        self.button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.guesses_remaining -= 1

        if guess == self.secret_number:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            self.master.quit()
        else:
            if guess < self.secret_number:
                message = "Too low! "
            else:
                message = "Too high! "
            
            if self.guesses_remaining > 0:
                message += f"You have {self.guesses_remaining} guesses left."
            else:
                message += f"Sorry, you're out of guesses. The number was {self.secret_number}."
                self.master.quit()
            
            messagebox.showwarning("Incorrect Guess", message)

# Create the main window
root = tk.Tk()
root.configure(bg='#0000ff')  # Set background color for the main window to blue
game = GuessTheNumberGame(root)
root.mainloop()