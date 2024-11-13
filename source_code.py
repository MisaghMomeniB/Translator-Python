from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")
        self.root.geometry("1080x400")
        self.root.configure(bg="white")

        # Initialize Translator
        self.translator = Translator()

        # Load images (with error handling)
        self.load_images()

        # Set up language options
        self.language_options = list(LANGUAGES.values())

        # Initialize UI components
        self.create_widgets()

        # Start label updates
        self.update_labels()

    def load_images(self):
        try:
            self.root.iconphoto(False, PhotoImage(file="GT.png"))  # Adjust image file path
            self.arrow_image = PhotoImage(file="trns.png")  # Adjust image file path
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")
            self.arrow_image = None

    def create_widgets(self):
        # Source Language Combobox
        self.combobox_from_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_from_lang.place(x=10, y=20, width=200)
        self.combobox_from_lang.set("English")

        self.label1 = Label(self.root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label1.place(x=10, y=60)

        # Input Text Frame
        self.input_frame = Frame(self.root, bg="Black", bd=5)
        self.input_frame.place(x=10, y=120, width=440, height=200)

        self.text1 = Text(self.input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=430, height=200)

        self.scrollbar1 = Scrollbar(self.input_frame, command=self.text1.yview)
        self.scrollbar1.pack(side="right", fill="y")
        self.text1.configure(yscrollcommand=self.scrollbar1.set)

        # Target Language Combobox
        self.combobox_to_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_to_lang.place(x=800, y=20, width=200)
        self.combobox_to_lang.set("Select Language")

        self.label2 = Label(self.root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label2.place(x=620, y=60)

        # Output Text Frame
        self.output_frame = Frame(self.root, bg="Black", bd=5)
        self.output_frame.place(x=600, y=120, width=440, height=200)

        self.text2 = Text(self.output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text2.place(x=0, y=0, width=430, height=200)

        self.scrollbar2 = Scrollbar(self.output_frame, command=self.text2.yview)
        self.scrollbar2.pack(side="right", fill="y")
        self.text2.configure(yscrollcommand=self.scrollbar2.set)

        # Translate Button
        self.translate_button = Button(self.root, text="Translate", font="Arial 15 bold", bg="red", fg="white", bd=5,
                                       activebackground="purple", cursor="hand2", command=self.translate_text)
        self.translate_button.place(x=465, y=250, width=120, height=40)

        # Optional arrow image to display between language selection
        if self.arrow_image:
            image_label = Label(self.root, image=self.arrow_image, width=70, bg="white")
            image_label.place(x=500, y=60)

    def update_labels(self):
        self.label1.configure(text=self.combobox_from_lang.get())
        self.label2.configure(text=self.combobox_to_lang.get())
        self.root.after(1000, self.update_labels)

    def translate_text(self):
        input_text = self.text1.get(1.0, END).strip()
        from_lang = self.combobox_from_lang.get()
        to_lang = self.combobox_to_lang.get()

        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        try:
            # Detect language and translate
            detected_lang = self.translator.detect(input_text).lang
            to_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)]

            translated_text = self.translator.translate(input_text, src=detected_lang, dest=to_lang_code).text
            self.text2.delete(1.0, END)
            self.text2.insert(END, translated_text)

        except Exception as e:
            messagebox.showerror("Translation Error", f"Could not translate the text.\nError: {str(e)}")

# Create the main Tkinter window
root = Tk()
app = TranslatorApp(root)

# Start the Tkinter main loop
root.mainloop()