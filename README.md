### Importing Libraries
```python
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
```
- `tkinter` is used to build the graphical user interface (GUI).
- `ttk` provides themed widgets for a modern look.
- `messagebox` provides dialog boxes for warnings or errors.
- `googletrans` gives access to Google Translate’s language options and a `Translator` object to handle the actual translation.

### Defining the TranslatorApp Class
```python
class TranslatorApp:
```
- This class creates the main application window and the translation logic.

#### Initializing the App
```python
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")
        self.root.geometry("1080x400")
        self.root.configure(bg="white")
```
- The constructor method `__init__` initializes the main application window. It sets the window title, size, and background color.

#### Setting Up Google Translator
```python
        self.translator = Translator()
```
- Initializes a `Translator` object from `googletrans`, which is used for translating text.

#### Loading Images
```python
        self.load_images()
```
- Calls a method to load images (e.g., an icon and an arrow image), with error handling in case images cannot be found.

#### Defining Language Options
```python
        self.language_options = list(LANGUAGES.values())
```
- Retrieves the list of available languages from `googletrans` and stores it for use in language selection dropdowns.

#### Setting Up UI Widgets
```python
        self.create_widgets()
```
- Calls a method to set up all UI components (e.g., labels, comboboxes, text areas, and buttons).

#### Updating Language Labels
```python
        self.update_labels()
```
- Calls a method to keep the labels updated based on the selected languages.

### Loading Images
```python
    def load_images(self):
```
- This method attempts to load images such as the app icon and an arrow image.

```python
        try:
            self.root.iconphoto(False, PhotoImage(file="GT.png"))
            self.arrow_image = PhotoImage(file="trns.png")
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")
            self.arrow_image = None
```
- The `try` block attempts to load images and set an icon for the window.
- If any image file is missing or cannot load, an error message is shown, and `self.arrow_image` is set to `None`.

### Creating UI Widgets
```python
    def create_widgets(self):
```
- This method sets up all UI elements (labels, comboboxes, text areas, and buttons) for the translation app.

#### Source Language Combobox
```python
        self.combobox_from_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_from_lang.place(x=10, y=20, width=200)
        self.combobox_from_lang.set("English")
```
- Creates a combobox (`combobox_from_lang`) for selecting the source language.
- The default language is set to “English.”

#### Source Language Label
```python
        self.label1 = Label(self.root, text="English", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label1.place(x=10, y=60)
```
- Displays the current source language as a label (`label1`).

#### Input Text Area
```python
        self.input_frame = Frame(self.root, bg="Black", bd=5)
        self.input_frame.place(x=10, y=120, width=440, height=200)

        self.text1 = Text(self.input_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=430, height=200)
```
- Creates a frame and text area (`text1`) for users to input text for translation.

#### Scrollbar for Input Text Area
```python
        self.scrollbar1 = Scrollbar(self.input_frame, command=self.text1.yview)
        self.scrollbar1.pack(side="right", fill="y")
        self.text1.configure(yscrollcommand=self.scrollbar1.set)
```
- Adds a scrollbar to the input text area to enable scrolling when there is a large amount of text.

#### Target Language Combobox
```python
        self.combobox_to_lang = ttk.Combobox(self.root, values=self.language_options, font="Arial 14", state="readonly")
        self.combobox_to_lang.place(x=800, y=20, width=200)
        self.combobox_to_lang.set("Select Language")
```
- Sets up another combobox (`combobox_to_lang`) for the target language selection. The default display is “Select Language.”

#### Target Language Label
```python
        self.label2 = Label(self.root, text="Select Language", font="Arial 30 bold", bg="white", width=18, bd=5, relief="groove")
        self.label2.place(x=620, y=60)
```
- Displays the selected target language in a label (`label2`).

#### Output Text Area
```python
        self.output_frame = Frame(self.root, bg="Black", bd=5)
        self.output_frame.place(x=600, y=120, width=440, height=200)

        self.text2 = Text(self.output_frame, font="Arial 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text2.place(x=0, y=0, width=430, height=200)
```
- Creates a frame and text area (`text2`) for displaying the translated text.

#### Scrollbar for Output Text Area
```python
        self.scrollbar2 = Scrollbar(self.output_frame, command=self.text2.yview)
        self.scrollbar2.pack(side="right", fill="y")
        self.text2.configure(yscrollcommand=self.scrollbar2.set)
```
- Adds a scrollbar to the output text area to accommodate long translated texts.

#### Translate Button
```python
        self.translate_button = Button(self.root, text="Translate", font="Arial 15 bold", bg="red", fg="white", bd=5,
                                       activebackground="purple", cursor="hand2", command=self.translate_text)
        self.translate_button.place(x=465, y=250, width=120, height=40)
```
- Adds a button to trigger the translation, styled with colors and fonts.

#### Optional Arrow Image
```python
        if self.arrow_image:
            image_label = Label(self.root, image=self.arrow_image, width=70, bg="white")
            image_label.place(x=500, y=60)
```
- Displays an optional arrow image between the source and target language comboboxes if the image loaded successfully.

### Updating Language Labels
```python
    def update_labels(self):
        self.label1.configure(text=self.combobox_from_lang.get())
        self.label2.configure(text=self.combobox_to_lang.get())
        self.root.after(1000, self.update_labels)
```
- Updates `label1` and `label2` to reflect the current selections in the source and target language comboboxes, refreshing every second.

### Performing Translation
```python
    def translate_text(self):
```
- This method handles the translation process.

#### Retrieving Input
```python
        input_text = self.text1.get(1.0, END).strip()
        from_lang = self.combobox_from_lang.get()
        to_lang = self.combobox_to_lang.get()
```
- Extracts the input text, source language, and target language from the respective UI elements.

#### Checking for Empty Input
```python
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return
```
- Displays a warning if no input text is provided.

#### Translating the Text
```python
        try:
            detected_lang = self.translator.detect(input_text).lang
            to_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)]
            translated_text = self.translator.translate(input_text, src=detected_lang, dest=to_lang_code).text
```
- Detects the input text language automatically and retrieves the language code for the target language.
- Uses `translator.translate()` to perform the translation and stores the result.

#### Displaying Translated Text
```python
            self.text2.delete(1.0, END)
            self.text2.insert(END, translated_text)
```
- Clears the output text area and inserts the translated text.

#### Handling Errors
```python
        except Exception as e:
            messagebox.showerror("Translation Error", f"Could not translate the text.\nError: {str(e)}")
```
- If an error occurs during translation, displays an error message.

### Running the Application
```python
root = Tk()
app = TranslatorApp(root)
root.mainloop()
```
- Initializes the Tkinter application window and runs the main loop, making the app window interactive.
