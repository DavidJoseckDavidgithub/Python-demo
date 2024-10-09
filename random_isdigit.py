import random
import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the leaderboard file
LEADERBOARD_FILE = "leaderboard.json"

# Load leaderboard from file
def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
        return {}

    # Save leaderboard to file
    def save_leaderboard(leaderboard):
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(leaderboard, f)

    # Difficulty levels
    def get_range(level):
        if level == "Easy":
            return 10
        elif level == "Medium":
            return 50
        elif level == "hard":
            return 100
        elif level == "Complex":
            return 1000
        else:
            return 10  # Default range if no valid level is selected

class Number_Guessing_Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")  # Optional: Set window size
        self.master.resizable(False, False)  # Prevent window resizing

        self.level = tk.StringVar(value="Easy")  # Set default difficulty
        self.guess_count = 0
        self.random_number = 0

        # Create UI elements
        self.create_widgets()

        # Load the leaderboard at initialization
        self.leaderboard = load_leaderboard()

    def create_widgets(self):
        # Difficulty Level Selection
        level_frame = tk.Frame(self.master)
        level_frame.pack(pady=10)

        tk.Label(level_frame, text="Select Difficulty:").pack(side=tk.LEFT, padx=5)

        levels = ["Easy", "Medium", "Hard", "Complex"]
        for lvl in levels:
            tk.Radiobutton(level_frame, text=lvl, variable=self.level, value=lvl).pack(side=tk.LEFT)

        # Start Game Button
        start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        start_button.pack(pady=10)

        # Entry for user's guess
        guess_frame = tk.Frame(self.master)
        guess_frame.pack(pady=10)

        tk.Label(guess_frame, text="Enter your guess:").pack(side=tk.LEFT, padx=5)
        self.guess_entry = tk.Entry(guess_frame)
        self.guess_entry.pack(side=tk.LEFT)

        # Submit Guess Button
        submit_button = tk.Button(self.master, text="Submit Guess", command=self.submit_guess)
        submit_button.pack(pady=5)

        # Feedback Label
        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Leaderboard Button
        leaderboard_button = tk.Button(self.master, text="View Leaderboard", command=self.show_leaderboard)
        leaderboard_button.pack(pady=5)

        # Initially disable guess submission until game starts
        self.toggle_guess_widgets(state="disabled")

        tk.Button(self.master, text="Start Game", command=self.start_game).pack()

    def toggle_guess_widgets(self, state):
        """Enable or disable guess entry and submit button."""
        self.guess_entry.config(state=state)
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'] == "Submit Guess":
                widget.config(state=state)

    def start_game(self):
        """Initialize or reset the game."""
        self.guess_count = 0
        range_max = get_range(self.level.get())
        self.random_number = random.randint(1, range_max)
        self.result_label.config(text=f"Guess a number between 1 and {range_max}.")
        self.guess_entry.delete(0, tk.END)
        self.toggle_guess_widgets(state="normal")
        self.guess_entry.focus_set()  # Focus on the guess entry field

    def submit_guess(self):
        """Handle the user's guess."""
        guess = self.guess_entry.get()

        # Input Validation
        if not guess.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            self.guess_entry.delete(0, tk.END)
            return

        guess = int(guess)
        self.guess_count += 1
        range_max = get_range(self.level.get())

        # Check if guess is within range
        if guess < 1 or guess > range_max:
            messagebox.showwarning("Out of Range", f"Please guess a number between 1 and {range_max}.")
            self.guess_entry.delete(0, tk.END)
            return

        # Compare guess with the random number
        if guess < self.random_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.random_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You've guessed the number in {self.guess_count} tries.")
            self.toggle_guess_widgets(state="disabled")
            self.update_leaderboard()

        self.guess_entry.delete(0, tk.END)

    def update_leaderboard(self):
        """Update the leaderboard with the current player's score."""
        name = simpledialog.askstring("Name", "Enter your name for the leaderboard:")
        if not name:
            name = "Anonymous"

        level = self.level.get()
        scorre = self.guess_count

        # Initialize leaderboard structure if not present
        if level not in self.leaderboard:
            self.leaderboard[level] = []


        # Append the new score
        self.leaderboard[level].append({'name': name, 'score': score})

        # Sort the leaderboard for the level based on score
        self.leaderboard[level] = sorted(self.leaderboard[level], key=lambda x: x['score'])[:5]  # Keep top 5

        save_leaderboard(self.leaderboard)
        messagebox.showinfo("Well Done!", f"Your score has been recorded, {name}!")
        self.show_leaderboard()

    def show_leaderboard(self):
        """Display the current leaderboard."""
        if not self.leaderboard:
            messagebox.showinfo("Leaderboard", "No high scores yet.")
            return

        leaderboard_text = ""
        for level, scores in self.leaderboard.items():
            leaderboard_text += f"\n{level}:\n"
            for entry in scores:
                leaderboard_text += f"  {entry['name']} - {entry['score']} guesses\n"

        messagebox.showinfo("Leaderboard", leaderboard_text)
    def reset_leaderboard(self):
        """Reset the leaderboard after confirmation."""
        if messagebox.askyesno("Reset Leaderboard", "Are you sure you want to reset the leaderboard?"):
            self.leaderboard = {}
            save_leaderboard(self.leaderboard)
            messagebox.showinfo("Reset Leaderboard", "Leaderboard has been reset.")


def main():
        root = tk.Tk()
        game = NumberGuessingGame(root)
        root.mainloop()

if __name__ == "__main__":
    main()
