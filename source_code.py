from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator

# Initialize the main application window
root = Tk()
root.title("Translator")
root.geometry("1080x400")
root.configure(bg="white")

# Initialize the Translator
translator = Translator()

# Function to update language labels based on the selected languages
def update_labels():
    label1.configure(text=combobox_from_lang.get())
    label2.configure(text=combobox_to_lang.get())
    root.after(1000, update_labels)

# Function to perform the translation
def translate_text():
    input_text = text1.get(1.0, END).strip()
    from_lang = combobox_from_lang.get()
    to_lang = combobox_to_lang.get()

    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        # Detect language and translate
        detected_lang = translator.detect(input_text).lang
        to_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)]

        translated_text = translator.translate(input_text, src=detected_lang, dest=to_lang_code).text
        text2.delete(1.0, END)
        text2.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"Could not translate the text.\nError: {str(e)}")

# Load and set images, handling errors if not found
try:
    root.iconphoto(False, PhotoImage(file="GT.png"))  # Adjust image file path
    arrow_image = PhotoImage(file="trns.png")  # Adjust image file path
except Exception as e:
    messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")

# Language options for comboboxes
language_options = list(LANGUAGES.values())

# Source Language Combobox
combobox_from_lang = ttk.Combobox(root, values=language_options, font="Arial 14", state="readonly")
combobox_from_lang.place(x=10, y=20, width=200)
combobox_from_lang.set("English")

label1 = Label(root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
label1.place(x=10, y=60)

# Input Text Frame
input_frame = Frame(root, bg="Black", bd=5)
input_frame.place(x=10, y=120, width=440, height=200)

text1 = Text(input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(input_frame, command=text1.yview)
scrollbar1.pack(side="right", fill="y")
text1.configure(yscrollcommand=scrollbar1.set)

# Target Language Combobox
combobox_to_lang = ttk.Combobox(root, values=language_options, font="Arial 14", state="readonly")
combobox_to_lang.place(x=800, y=20, width=200)
combobox_to_lang.set("Select Language")

label2 = Label(root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
label2.place(x=620, y=60)

# Output Text Frame
output_frame = Frame(root, bg="Black", bd=5)
output_frame.place(x=600, y=120, width=440, height=200)

text2 = Text(output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(output_frame, command=text2.yview)
scrollbar2.pack(side="right", fill="y")
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button
translate_button = Button(root, text="Translate", font="Arial 15 bold", bg="red", fg="white", bd=5,
                          activebackground="purple", cursor="hand2", command=translate_text)
translate_button.place(x=465, y=250, width=120, height=40)

# Optional arrow image to display between language selection
# Uncomment if "arrow_image" is loaded successfully
if 'arrow_image' in locals():
    image_label = Label(root, image=arrow_image, width=70, bg="white")
    image_label.place(x=500, y=60)

# Start label updates
update_labels()

# Start the Tkinter main loop
root.mainloop()