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

# Create and place the first language combobox (source language)
combbol1 = ttk.Combobox(root, values=languageV, font="Arial 14", state="readonly")
combbol1.place(x=10, y=20, width=200)
combbol1.set("English")  # Set default value

label1 = Label(root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
label1.place(x=10, y=60)  # Position the label

# Frame for input text
input_frame = Frame(root, bg="Black", bd=5)
input_frame.place(x=10, y=120, width=440, height=200)

text1 = Text(input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)  # Input text area
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(input_frame, command=text1.yview)  # Scrollbar for input text
scrollbar1.pack(side="right", fill="y")
text1.configure(yscrollcommand=scrollbar1.set)  # Link scrollbar with text area

# Create and place the second language combobox (target language)
combbol2 = ttk.Combobox(root, values=languageV, font="Arial 14", state="readonly")
combbol2.place(x=800, y=20, width=200)
combbol2.set("Select Language")  # Set default value

label2 = Label(root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
label2.place(x=620, y=60)  # Position the label

# Frame for output text
output_frame = Frame(root, bg="Black", bd=5)
output_frame.place(x=600, y=120, width=440, height=200)

text2 = Text(output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)  # Output text area
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(output_frame, command=text2.yview)  # Scrollbar for output text
scrollbar2.pack(side="right", fill="y")
text2.configure(yscrollcommand=scrollbar2.set)  # Link scrollbar with text area

# Translate button
translate = Button(root, text="Translate", font="Arial 15 bold", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=465, y=250, width=120, height=40)  # Position the button and set its size