from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator

# Define the main Translator App class
class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")              # Set window title
        self.root.geometry("1080x500")             # Set window size
        self.root.configure(bg="white")            # Set background color

        self.translator = Translator()             # Initialize the translator object
        self.load_images()                         # Load app and arrow icons

        self.language_options = list(LANGUAGES.values())  # List of available languages
        self.create_widgets()                      # Create all UI components
        self.update_labels()                       # Update source/target language labels dynamically

    # Load icons for the app and the UI
    def load_images(self):
        try:
            self.root.iconphoto(False, PhotoImage(file="GT.png"))  # App icon
            self.arrow_image = PhotoImage(file="trns.png")         # Optional arrow image
        except:
            self.arrow_image = None                                # Set to None if image fails to load

    # Build all UI widgets
    def create_widgets(self):
        # Source language dropdown
        self.combobox_from_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_from_lang.place(x=10, y=20, width=200)
        self.combobox_from_lang.set("English")

        # Label for source language
        self.label1 = Label(self.root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label1.place(x=10, y=60)

        # Input text frame
        self.input_frame = Frame(self.root, bg="Black", bd=5)
        self.input_frame.place(x=10, y=120, width=440, height=200)

        # Input text area
        self.text1 = Text(self.input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=430, height=200)

        # Scrollbar for input
        self.scrollbar1 = Scrollbar(self.input_frame, command=self.text1.yview)
        self.scrollbar1.pack(side="right", fill="y")
        self.text1.configure(yscrollcommand=self.scrollbar1.set)

        # Target language dropdown
        self.combobox_to_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_to_lang.place(x=800, y=20, width=200)
        self.combobox_to_lang.set("Select Language")

        # Label for target language
        self.label2 = Label(self.root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label2.place(x=620, y=60)

        # Output text frame
        self.output_frame = Frame(self.root, bg="Black", bd=5)
        self.output_frame.place(x=600, y=120, width=440, height=200)

        # Output text area
        self.text2 = Text(self.output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text2.place(x=0, y=0, width=430, height=200)

        # Scrollbar for output
        self.scrollbar2 = Scrollbar(self.output_frame, command=self.text2.yview)
        self.scrollbar2.pack(side="right", fill="y")
        self.text2.configure(yscrollcommand=self.scrollbar2.set)

        # Translate button
        self.translate_button = Button(self.root, text="Translate", font="Arial 15 bold", bg="red", fg="white", bd=5,
                                       activebackground="purple", cursor="hand2", command=self.translate_text)
        self.translate_button.place(x=465, y=250, width=120, height=40)

        # Clear button to reset both text areas
        self.clear_button = Button(self.root, text="Clear", font="Arial 15 bold", bg="gray", fg="white", bd=5,
                                   activebackground="darkgray", cursor="hand2", command=self.clear_text)
        self.clear_button.place(x=465, y=300, width=120, height=40)

        # Auto detect source language checkbox
        self.auto_detect_var = IntVar()
        self.auto_detect_check = Checkbutton(self.root, text="Auto Detect Language", font="Arial 12", variable=self.auto_detect_var, bg="white")
        self.auto_detect_check.place(x=10, y=340)

        # Display arrow image if available
        if self.arrow_image:
            image_label = Label(self.root, image=self.arrow_image, width=70, bg="white")
            image_label.place(x=500, y=60)

    # Update source and target language labels every second
    def update_labels(self):
        self.label1.configure(text=self.combobox_from_lang.get())
        self.label2.configure(text=self.combobox_to_lang.get())
        self.root.after(1000, self.update_labels)

    # Perform translation when Translate button is clicked
    def translate_text(self):
        input_text = self.text1.get(1.0, END).strip()
        from_lang = self.combobox_from_lang.get()
        to_lang = self.combobox_to_lang.get()

        # Warn if input is empty
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        # Warn if target language is not selected
        if to_lang == "Select Language":
            messagebox.showwarning("Warning", "Please select a target language.")
            return

        try:
            # Auto-detect source language if checkbox is selected
            if self.auto_detect_var.get():
                detected_lang = self.translator.detect(input_text).lang
                from_lang_code = detected_lang
            else:
                from_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(from_lang)]

            # Get language code for target language
            to_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)]

            # Perform translation
            translated_text = self.translator.translate(input_text, src=from_lang_code, dest=to_lang_code).text

            # Display result in output area
            self.text2.delete(1.0, END)
            self.text2.insert(END, translated_text)

        except Exception as e:
            messagebox.showerror("Translation Error", f"Could not translate the text.\nError: {str(e)}")

    # Clear both input and output text areas
    def clear_text(self):
        self.text1.delete(1.0, END)
        self.text2.delete(1.0, END)

# Create and run the app
root = Tk()
app = TranslatorApp(root)
root.mainloop()