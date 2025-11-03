# create a question
# create a delay with the time module
# create a list of answers
# generate a random number with the random module
# use taht random number to call the value of the index the list.

from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import random

responses =[
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Definitely",
    "Don’t count on it",
    "Without a doubt",
    "Very doubtful",
    "It is certain",
    "Outlook not so good",
    "Signs point to yes",
    "Better not tell you now",
    "Yes, absolutely",
    "My sources say no",
    "You may rely on it",
    "Reply hazy, try again",
    "Concentrate and ask again",
    "Outlook good",
    "Most likely",
    "Cannot predict now"
]

#----------------------NON-GUI VERSION-------------------
# question = input("Please enter your question: ")
# print ("thinking...")
# time.sleep(3)
# response = random.randrange(0,21)
# print(f"{responses[response]}")

#----------------------GUI VERSION-------------------

root = tk.Tk() # instance of the Tk classc
root.geometry("400x400") # set the window size
container = ttk.Frame(root, padding = 10)


root.title("Magic 8 Ball") # set the window title

# You can also add a label to describe the input field
label = ttk.Label(root, text="Enter your question:")
label.pack()

# Create a ttk.Entry widget
# The first argument is the master widget (the window or frame it belongs to)
entry_widget = ttk.Entry(root, width=30) # You can set the width in characters
entry_widget.pack(pady=10) # Place the widget in the window


# Function to get the input from the entry widget and display response
def get_response():
    
    # Add other content to your main window below the header
    content_label = tk.Label(root, text="thinking...")
    content_label.pack(pady=5)
    container.update()
    time.sleep(3)
    content_label.destroy()
    
    response = random.randrange(0,21)
    question = entry_widget.get()
    question_label = tk.Label(root, text=f"Your question: {question}")
    question_label.pack(pady=1)
    
    response_label = tk.Label(root, text=f"Prediction: {responses[response]}")
    response_label.pack(pady=1)

    divider = tk.Label(root, text=f" ")
    divider.pack(pady=5)
    response_label.update()

# Function to clear the entry widget
def clear_response():
    entry_widget.delete(0, tk.END)
    
# Function to play again
def play_again():
    entry_widget.delete(0, tk.END)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget != label:
            widget.destroy()

# Function to quit the app
def quit_app():
    root.destroy()            


# Create a button to trigger the input retrieval
ask_button = ttk.Button(root, text="Ask", command=get_response)
ask_button.pack(pady=5)
# In Tkinter, pack() is a geometry manager used to arrange widgets within a window or frame. It's one of three main geometry managers in Tkinter, alongside grid() and place()
# Create a button to trigger the input retrieval
clear_button = ttk.Button(root, text="Clear", command=clear_response)
clear_button.pack(pady=5)
play_again_button = ttk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=5)
quit_button = ttk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=5)

root.mainloop()
