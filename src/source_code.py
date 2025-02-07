from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator

# Define the main class for the Translator App
class TranslatorApp:
    def __init__(self, root):
        # This method initializes the main application window and its components.
        self.root = root
        self.root.title("Translator")  # Set the window title
        self.root.geometry("1080x400")  # Set the window size
        self.root.configure(bg="white")  # Set the background color of the window

        # Initialize the Translator object from googletrans library
        self.translator = Translator()

        # Load images (error handling to ensure images exist)
        self.load_images()

        # List of available languages from the googletrans library
        self.language_options = list(LANGUAGES.values())

        # Initialize the user interface components
        self.create_widgets()

        # Start label updates
        self.update_labels()

    def load_images(self):
        # This method loads images and handles any potential errors.
        try:
            # Set the app icon (the file path should be correct for your project)
            self.root.iconphoto(False, PhotoImage(file="GT.png"))
            self.arrow_image = PhotoImage(file="trns.png")  # Load the arrow image (this is optional)
        except Exception as e:
            # If images are not found or there is any error loading them, show an error message.
            messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")
            self.arrow_image = None  # Set arrow_image to None in case of error

    def create_widgets(self):
        # This method creates all the UI components for the translator app.

        # Source Language Combobox (for selecting the language from which to translate)
        self.combobox_from_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_from_lang.place(x=10, y=20, width=200)  # Position the combobox
        self.combobox_from_lang.set("English")  # Set the default source language to "English"

        # Label for the source language
        self.label1 = Label(self.root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label1.place(x=10, y=60)  # Position the label

        # Frame for the input text area
        self.input_frame = Frame(self.root, bg="Black", bd=5)
        self.input_frame.place(x=10, y=120, width=440, height=200)

        # Text area for entering the text to translate
        self.text1 = Text(self.input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=430, height=200)

        # Scrollbar for the input text area
        self.scrollbar1 = Scrollbar(self.input_frame, command=self.text1.yview)
        self.scrollbar1.pack(side="right", fill="y")  # Position the scrollbar
        self.text1.configure(yscrollcommand=self.scrollbar1.set)  # Link scrollbar with text box

        # Target Language Combobox (for selecting the language to translate into)
        self.combobox_to_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_to_lang.place(x=800, y=20, width=200)  # Position the combobox
        self.combobox_to_lang.set("Select Language")  # Set the default target language to "Select Language"

        # Label for the target language
        self.label2 = Label(self.root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label2.place(x=620, y=60)  # Position the label

        # Frame for the output text area
        self.output_frame = Frame(self.root, bg="Black", bd=5)
        self.output_frame.place(x=600, y=120, width=440, height=200)

        # Text area for displaying the translated text
        self.text2 = Text(self.output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text2.place(x=0, y=0, width=430, height=200)

        # Scrollbar for the output text area
        self.scrollbar2 = Scrollbar(self.output_frame, command=self.text2.yview)
        self.scrollbar2.pack(side="right", fill="y")  # Position the scrollbar
        self.text2.configure(yscrollcommand=self.scrollbar2.set)  # Link scrollbar with text box

        # Button to trigger translation
        self.translate_button = Button(self.root, text="Translate", font="Arial 15 bold", bg="red", fg="white", bd=5,
                                       activebackground="purple", cursor="hand2", command=self.translate_text)
        self.translate_button.place(x=465, y=250, width=120, height=40)  # Position the button

        # Optional arrow image displayed between the language selection comboboxes
        if self.arrow_image:
            image_label = Label(self.root, image=self.arrow_image, width=70, bg="white")
            image_label.place(x=500, y=60)  # Position the image label

    def update_labels(self):
        # This method updates the labels showing the selected source and target languages.
        self.label1.configure(text=self.combobox_from_lang.get())  # Update the source language label
        self.label2.configure(text=self.combobox_to_lang.get())  # Update the target language label
        self.root.after(1000, self.update_labels)  # Update labels every second

    def translate_text(self):
        # This method performs the actual translation.
        input_text = self.text1.get(1.0, END).strip()  # Get the input text and remove extra spaces
        from_lang = self.combobox_from_lang.get()  # Get the selected source language
        to_lang = self.combobox_to_lang.get()  # Get the selected target language

        # If no text was entered, show a warning message
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        try:
            # Detect the language of the input text using the translator
            detected_lang = self.translator.detect(input_text).lang
            # Get the corresponding language code for the target language
            to_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)]

            # Translate the text using the googletrans library
            translated_text = self.translator.translate(input_text, src=detected_lang, dest=to_lang_code).text

            # Display the translated text in the output text area
            self.text2.delete(1.0, END)  # Clear any existing text in the output area
            self.text2.insert(END, translated_text)  # Insert the translated text

        except Exception as e:
            # If an error occurs during translation, show an error message
            messagebox.showerror("Translation Error", f"Could not translate the text.\nError: {str(e)}")

# Create the main Tkinter window
root = Tk()
app = TranslatorApp(root)  # Create an instance of the TranslatorApp class

# Start the Tkinter main loop to run the application
root.mainloop()