from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator

# Create the main application window
root = Tk()
root.title("Translator")
root.geometry("1080x400")  # Set window size
root.configure(bg="white")  # Set background color

# Initialize the Translator
translator = Translator()

# Function to update language labels
def label_change():
    # Get selected languages
    from_lang = combbol1.get()
    to_lang = combbol2.get()
    # Update the labels with selected languages
    label1.configure(text=from_lang)
    label2.configure(text=to_lang)
    # Repeat the function every second
    root.after(1000, label_change)