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

# Function to perform the translation
def translate_now():
    try:
        # Get the input text from the text area
        text_ = text1.get(1.0, END).strip()
        from_lang = combbol1.get()  # Get the selected source language
        to_lang = combbol2.get()  # Get the selected target language

        # Check if the input text is empty
        if not text_:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return  # Exit the function if input is empty

        # Detect the language of the input text
        detected_lang = translator.detect(text_).lang
        if detected_lang not in LANGUAGES.keys():
            messagebox.showerror("Error", "Detected language is invalid.")
            return  # Exit the function if the detected language is invalid

        # Translate the text
        translated = translator.translate(text_, src=detected_lang, dest=list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)])
        
        # Display the translated text in the output text area
        text2.delete(1.0, END)  # Clear previous output
        text2.insert(END, translated.text)  # Insert the translated text

    except Exception as e:
        # Show an error message in case of an exception
        messagebox.showerror("Translation Error", f"Could not translate the text. Please try again.\nError: {str(e)}")

# Load images for the application
try:
    image_icon = PhotoImage(file="GT.png")  # Load the icon image
    root.iconphoto(False, image_icon)  # Set window icon
    arrow_image = PhotoImage(file="trns.png")  # Load the arrow image
except Exception as e:
    messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")  # Handle image loading errors

# Language options
language = LANGUAGES
languageV = list(language.values())  # List of language names