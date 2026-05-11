import tkinter as tk
import time
import random

class TypingSpeedTester:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Tester")

        self.words = self.load_words("common_words.txt")  # Load words from a file
        self.current_text = random.choice(self.words)
        self.start_time = 0
        self.typed_chars = 0
        self.correct_chars = 0
        self.running = False

        self.instruction_label = tk.Label(master, text="Type the following text:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.text_label = tk.Label(master, text=self.current_text, font=("Arial", 12), wraplength=400)
        self.text_label.pack(pady=5)

        self.entry = tk.Text(master, height=5, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_typing)

        self.start_button = tk.Button(master, text="Start", command=self.start_test, font=("Arial", 12))
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.time_label = tk.Label(master, text="Time: 0.00 s", font=("Arial", 12))
        self.time_label.pack()

    def load_words(self, filename="common_words.txt"):
        """Loads a list of common words from a file."""
        try:
            with open(filename, "r") as f:
                words = [word.strip() for word in f.readlines()]
            return words
        except FileNotFoundError:
            return ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog",
                    "python", "programming", "tkinter", "gui", "application", "test", "speed",
                    "accuracy", "timer", "interface", "build", "code", "example"]

    def start_test(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.typed_chars = 0
            self.correct_chars = 0
            self.current_text = random.choice(self.words)
            self.text_label.config(text=self.current_text)
            self.entry.delete("1.0", tk.END)
            self.result_label.config(text="")
            self.update_timer()
            self.entry.config(state=tk.NORMAL)
            self.start_button.config(state=tk.DISABLED, text="Running...")

    def update_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {elapsed_time:.2f} s")
            self.master.after(100, self.update_timer)

    def check_typing(self, event):
        if self.running:
            typed_text = self.entry.get("1.0", tk.END).strip()
            self.typed_chars = len(typed_text)
            self.correct_chars = 0
            for i, char in enumerate(typed_text):
                if i < len(self.current_text) and char == self.current_text[i]:
                    self.correct_chars += 1

            if typed_text == self.current_text:
                self.end_test()

    def end_test(self):
        self.running = False
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 0:
            words_typed = len(self.current_text.split())
            wpm = int((words_typed / elapsed_time) * 60)
            accuracy = (self.correct_chars / len(self.current_text)) * 100
            self.result_label.config(text=f"Speed: {wpm} WPM\nAccuracy: {accuracy:.2f}%")
        else:
            self.result_label.config(text="Time elapsed is too short to calculate.")
        self.start_button.config(state=tk.NORMAL, text="Restart")
        self.entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root
    root.mainloop()
