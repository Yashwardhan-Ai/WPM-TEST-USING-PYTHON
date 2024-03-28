import time
import random
from tkinter import *

# Function to choose a random word from a list
def get_word():
    words = ["education is must", "python is fantastic", "speedup or else someone will surpass you", "test your abilities", "typing is an essential skill", "practice makes man perfect", "accuracy", "keyboard"]
    return random.choice(words)

# Function to start the test
def start_test(event):
    global start_time
    start_time = time.time()
    word_entry.config(state=NORMAL)
    word_entry.delete(0, END)
    test_button.config(state=DISABLED)
    random_word.set(get_word())

# Function to calculate WPM and end the test
def end_test():
    end_time = time.time()
    time_elapsed = end_time - start_time
    words_typed = word_entry.get().split(" ")
    word_count = len(words_typed)
    wpm = round((word_count / time_elapsed) * 60, 2)
    result_label.config(text=f"WPM: {wpm}")
    word_entry.config(state=DISABLED)
    test_button.config(state=NORMAL)

# GUI setup
root = Tk()
root.title("WPM Speed Test")

random_word = StringVar(root)
word_label = Label(root, textvariable=random_word, font=("Helvetica", 18))
word_label.pack()

word_entry = Entry(root)
word_entry.pack()
word_entry.config(state=DISABLED)
word_entry.bind("<Return>", lambda event: end_test())

test_button = Button(root, text="Start Test", command=lambda: start_test(None))
test_button.pack()

result_label = Label(root, text="", font=("Helvetica", 18))
result_label.pack()

root.mainloop()