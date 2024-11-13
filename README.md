__Hello My Friend 👋🏻__ <br>
__I'm Misagh and I'm Glad You're Here 😉__

# Translator-Python🐍
I Wrote a Translator Using __Python__. I Built the Graphical Interface of This Program With ***Tkinter***. It is a Regular Translator That You Can Use for Any Language You Want.

# Does It Require Any Installation Steps or Prerequisites?
__Debian / Ubuntu__ <br>
`` sudo apt-get install python3-tk `` <br>

__Fedora__ <br>
`` sudo dnf install python3-tkinte `` <br>

`` pip install googletrans==4.0.0-rc1 ``

# Line-by-line Code Analysis

### Imports
```python
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
```
1. `from tkinter import *`: This imports all the necessary widgets and functions from the `tkinter` module to build the graphical user interface (GUI) of the application. This includes things like buttons, labels, and frames.
   
2. `from tkinter import ttk, messagebox`: 
   - `ttk` is used for themed widgets, which provide more modern and polished components like combo boxes (dropdowns) and buttons.
   - `messagebox` is used for displaying warning, error, and informational dialog boxes to the user.

3. `from googletrans import LANGUAGES, Translator`: 
   - `LANGUAGES`: This is a dictionary in the `googletrans` module, which maps language codes (e.g., 'en' for English) to the human-readable names of the languages (e.g., "English").
   - `Translator`: This is the core object used to interact with Google Translate for translating text.

---

### Class Definition: `TranslatorApp`
```python
class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator") 
        self.root.geometry("1080x400")  
        self.root.configure(bg="white")  
        
        self.translator = Translator()
        self.load_images()
        self.language_options = list(LANGUAGES.values())
        self.create_widgets()
        self.update_labels()
```
4. `class TranslatorApp:`: Defines a Python class called `TranslatorApp`, which encapsulates the entire functionality of the translation application.

5. `def __init__(self, root):`: This is the constructor method, which is automatically called when an object of the `TranslatorApp` class is instantiated. It initializes the main window and the various components of the application.

6. `self.root = root`: This stores the reference to the Tkinter root window (`root`) in an instance variable, allowing access to it throughout the class.

7. `self.root.title("Translator")`: Sets the title of the main application window to "Translator."

8. `self.root.geometry("1080x400")`: Specifies the size of the main application window (1080px wide by 400px high).

9. `self.root.configure(bg="white")`: Sets the background color of the application window to white.

10. `self.translator = Translator()`: Initializes a `Translator` object, which is used to perform the text translation.

11. `self.load_images()`: Calls a method to load images such as the app icon and optional arrow images.

12. `self.language_options = list(LANGUAGES.values())`: Creates a list of available language names (as strings) for the language dropdowns. It takes all values from the `LANGUAGES` dictionary.

13. `self.create_widgets()`: Calls another method to create the widgets (UI components) for the app.

14. `self.update_labels()`: Calls a method to periodically update the language labels showing the selected source and target languages.

---

### `load_images` Method
```python
def load_images(self):
    try:
        self.root.iconphoto(False, PhotoImage(file="GT.png"))
        self.arrow_image = PhotoImage(file="trns.png")
    except Exception as e:
        messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")
        self.arrow_image = None
```
15. `def load_images(self):`: This method loads images for the app's icon and any other images, such as the arrow used between language selection dropdowns.

16. `try:`: Starts a `try-except` block to handle potential errors when loading images.

17. `self.root.iconphoto(False, PhotoImage(file="GT.png"))`: Attempts to load the app icon from a file called `"GT.png"` and sets it as the icon for the Tkinter window (`root`).

18. `self.arrow_image = PhotoImage(file="trns.png")`: Attempts to load an image for the arrow (used to visually separate the language selection dropdowns) from a file called `"trns.png"`.

19. `except Exception as e:`: If there's an error (e.g., the images are not found), the program will catch the exception and execute the code below.

20. `messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")`: Displays an error message box indicating that the images could not be loaded.

21. `self.arrow_image = None`: Sets `self.arrow_image` to `None` in case the image loading fails.

---

### `create_widgets` Method
```python
def create_widgets(self):
    self.combobox_from_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
    self.combobox_from_lang.place(x=10, y=20, width=200)
    self.combobox_from_lang.set("English")
    self.label1 = Label(self.root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
    self.label1.place(x=10, y=60)
    
    self.input_frame = Frame(self.root, bg="Black", bd=5)
    self.input_frame.place(x=10, y=120, width=440, height=200)
    
    self.text1 = Text(self.input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
    self.text1.place(x=0, y=0, width=430, height=200)
    
    self.scrollbar1 = Scrollbar(self.input_frame, command=self.text1.yview)
    self.scrollbar1.pack(side="right", fill="y")
    self.text1.configure(yscrollcommand=self.scrollbar1.set)
    
    self.combobox_to_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
    self.combobox_to_lang.place(x=800, y=20, width=200)
    self.combobox_to_lang.set("Select Language")
    self.label2 = Label(self.root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
    self.label2.place(x=620, y=60)
    
    self.output_frame = Frame(self.root, bg="Black", bd=5)
    self.output_frame.place(x=600, y=120, width=440, height=200)
    
    self.text2 = Text(self.output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
    self.text2.place(x=0, y=0, width=430, height=200)
    
    self.scrollbar2 = Scrollbar(self.output_frame, command=self.text2.yview)
    self.scrollbar2.pack(side="right", fill="y")
    self.text2.configure(yscrollcommand=self.scrollbar2.set)
    
    self.translate_button = Button(self.root, text="Translate", font="Arial 15 bold", bg="red", fg="white", bd=5,
                                   activebackground="purple", cursor="hand2", command=self.translate_text)
    self.translate_button.place(x=465, y=250, width=120, height=40)
    
    if self.arrow_image:
        image_label = Label(self.root, image=self.arrow_image, width=70, bg="white")
        image_label.place(x=500, y=60)
```

This method creates and places all the widgets (UI elements) on the screen.

- **Source Language Dropdown (`combobox_from_lang`)**: A dropdown for selecting the source language. It is set to "English" by default.
- **Source Language Label (`label1`)**: A label showing the current source language, initially set to "English."
- **Input Text Area (`text1`)**: A text area where users enter text to be translated. A scrollbar is added for large text input.
- **Target Language Dropdown (`combobox_to_lang`)**: A dropdown for selecting the target language.
- **Target Language Label (`label2`)**: A label showing the currently selected target language, initially set to "Select Language."
- **Output Text Area (`text2`)**: A text area where the translated text will be displayed. A scrollbar is added for large output text.
- **Translate Button (`translate_button`)**: A button that, when clicked, calls the `translate_text` method to perform the translation.
- **Arrow Image (`image_label`)**: Optionally shows an arrow image between the source and target language selectors, if the image was successfully loaded.

---

### `update_labels` Method
```python
def update_labels(self):
    self.label1.configure(text=self.combobox_from_lang.get())
    self.label2.configure(text=self.combobox_to_lang.get())
    self.root.after(1000, self.update_labels)
```
- This method updates the labels (`label1` and `label2`) to reflect the currently selected source and target languages.
- `self.combobox_from_lang.get()` and `self.combobox_to_lang.get()` retrieve the selected languages from the dropdowns.
- `self.root.after(1000, self.update_labels)` makes the function call itself every 1000 milliseconds (1 second), continuously updating the labels.

---

### `translate_text` Method
```python
def translate_text(self):
    input_text = self.text1.get(1.0, END).

strip()
    from_lang = self.combobox_from_lang.get()
    to_lang = self.combobox_to_lang.get()

    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        detected_lang = self.translator.detect(input_text).lang
        to_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)]
        translated_text = self.translator.translate(input_text, src=detected_lang, dest=to_lang_code).text

        self.text2.delete(1.0, END)
        self.text2.insert(END, translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Could not translate the text.\nError: {str(e)}")
```

- This method handles the translation logic.
- `input_text` gets the text entered by the user in `text1`. `from_lang` and `to_lang` are the selected source and target languages.
- If no text is entered, it shows a warning message.
- The translation is performed using the `googletrans` API:
  - It detects the language of the input text with `self.translator.detect()`.
  - Then it translates the text using `self.translator.translate()`.
  - The translated text is inserted into `text2`.
- If an error occurs during translation, it displays an error message.

---

### Main Code to Run the Application
```python
root = Tk()
app = TranslatorApp(root)
root.mainloop()
```
- `root = Tk()`: Initializes the main Tkinter window (`root`).
- `app = TranslatorApp(root)`: Creates an instance of the `TranslatorApp` class, passing the `root` window to it.
- `root.mainloop()`: Starts the Tkinter event loop, which listens for user input (e.g., button clicks) and updates the GUI accordingly.

---
