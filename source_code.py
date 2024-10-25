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