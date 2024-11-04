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

### Importing Required Libraries
```python
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
```
- **`from tkinter import *`**: Imports all classes and functions from the `tkinter` module, which is used for building GUI applications in Python.
- **`from tkinter import ttk, messagebox`**: Imports the `ttk` module for themed widgets and `messagebox` for displaying alert dialogs.
- **`from googletrans import LANGUAGES, Translator`**: Imports the `LANGUAGES` dictionary (a mapping of language names to their codes) and the `Translator` class from the `googletrans` module, which provides translation capabilities.

### Setting Up the Main Application Window
```python
root = Tk()
root.title("Translator")
root.geometry("1080x400")  # Set window size
root.configure(bg="white")  # Set background color
```
- **`root = Tk()`**: Initializes the main window (the root widget).
- **`root.title("Translator")`**: Sets the title of the application window.
- **`root.geometry("1080x400")`**: Specifies the size of the window, which is 1080 pixels wide and 400 pixels tall.
- **`root.configure(bg="white")`**: Changes the background color of the window to white for better visibility and aesthetics.

### Initializing the Translator
```python
translator = Translator()
```
- **`translator = Translator()`**: Creates an instance of the `Translator` class, which will be used to perform translations throughout the application.

### Updating Language Labels
```python
def label_change():
    from_lang = combbol1.get()
    to_lang = combbol2.get()
    label1.configure(text=from_lang)
    label2.configure(text=to_lang)
    root.after(1000, label_change)
```
- **`def label_change():`**: Defines a function that updates the labels showing the selected languages.
- **`from_lang = combbol1.get()`**: Gets the currently selected source language from the first combobox.
- **`to_lang = combbol2.get()`**: Gets the currently selected target language from the second combobox.
- **`label1.configure(text=from_lang)`**: Updates the display label for the source language.
- **`label2.configure(text=to_lang)`**: Updates the display label for the target language.
- **`root.after(1000, label_change)`**: Sets a timer to call `label_change()` every 1000 milliseconds (1 second) to keep the labels updated.

### Performing Translation
```python
def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        from_lang = combbol1.get()  # Get the selected source language
        to_lang = combbol2.get()  # Get the selected target language

        if not text_:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        detected_lang = translator.detect(text_).lang
        if detected_lang not in LANGUAGES.keys():
            messagebox.showerror("Error", "Detected language is invalid.")
            return

        translated = translator.translate(text_, src=detected_lang, dest=list(LANGUAGES.keys())[list(LANGUAGES.values()).index(to_lang)])
        
        text2.delete(1.0, END)  # Clear previous output
        text2.insert(END, translated.text)  # Insert the translated text

    except Exception as e:
        messagebox.showerror("Translation Error", f"Could not translate the text. Please try again.\nError: {str(e)}")
```
- **`def translate_now():`**: Defines a function to handle the translation process when the "Translate" button is pressed.
- **`text_ = text1.get(1.0, END).strip()`**: Retrieves the input text from the first text area and removes any leading or trailing whitespace.
- **`from_lang = combbol1.get()`**: Gets the selected source language.
- **`to_lang = combbol2.get()`**: Gets the selected target language.
- **`if not text_:`**: Checks if the input text is empty. If it is, a warning message is shown.
- **`detected_lang = translator.detect(text_).lang`**: Uses the translator to detect the language of the input text.
- **`if detected_lang not in LANGUAGES.keys():`**: Validates that the detected language is supported.
- **`translated = translator.translate(...)`**: Performs the translation using the `translate` method of the `Translator` instance, specifying the source and destination languages.
- **`text2.delete(1.0, END)`**: Clears any previous output in the second text area.
- **`text2.insert(END, translated.text)`**: Displays the translated text in the second text area.
- **`except Exception as e:`**: Catches any exceptions that may occur during the translation process and shows an error message.

### Loading Images for the Application
```python
try:
    image_icon = PhotoImage(file="GT.png")  # Load the icon image
    root.iconphoto(False, image_icon)  # Set window icon
    arrow_image = PhotoImage(file="trns.png")  # Load the arrow image
except Exception as e:
    messagebox.showerror("Image Error", f"Could not load images.\nError: {str(e)}")
```
- **`try:`**: Attempts to load image files for the application.
- **`image_icon = PhotoImage(file="GT.png")`**: Loads an icon image to be used as the application’s icon.
- **`root.iconphoto(False, image_icon)`**: Sets the loaded image as the window's icon.
- **`arrow_image = PhotoImage(file="trns.png")`**: Loads an additional image (though it is not displayed in the UI).
- **`except Exception as e:`**: If an error occurs while loading the images, it shows an error message to the user.

### Language Options and User Interface Elements
```python
language = LANGUAGES
languageV = list(language.values())  # List of language names

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
```
- **`language = LANGUAGES`**: Assigns the dictionary of languages to the `language` variable.
- **`languageV = list(language.values())`**: Creates a list of language names to populate the comboboxes.
- **`combbol1 = ttk.Combobox(...)`**: Creates a combobox for selecting the source language, setting it to a default of "English."
- **`label1 = Label(...)`**: Creates a label to display the currently selected source language.
- **`input_frame = Frame(...)`**: Creates a frame for containing the input text area, with a black background.
- **`text1 = Text(...)`**: Creates a text area for user input, allowing for multiple lines and word wrapping.
- **`scrollbar1 = Scrollbar(...)`**: Adds a scrollbar

 to the input text area to handle overflow text.
- **`combbol2 = ttk.Combobox(...)`**: Creates a second combobox for selecting the target language, with a default setting of "Select Language."
- **`label2 = Label(...)`**: Creates a label for the target language selection.
- **`output_frame = Frame(...)`**: Creates a frame for displaying the translated text, similarly styled as the input frame.
- **`text2 = Text(...)`**: Creates a text area for displaying the translated output.
- **`scrollbar2 = Scrollbar(...)`**: Adds a scrollbar to the output text area.

### Translate Button
```python
translate = Button(root, text="Translate", font="Arial 15 bold", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=465, y=250, width=120, height=40)  # Position the button and set its size
```
- **`translate = Button(...)`**: Creates a button labeled "Translate," which will trigger the translation process when clicked. The button is styled with font, colors, and size settings.
- **`command=translate_now`**: Specifies that the `translate_now()` function should be called when the button is pressed.
- **`translate.place(...)`**: Positions the button at the specified coordinates and sets its size.

### Start the Application Loop
```python
label_change()  # Start the label updating loop
root.mainloop()  # Run the application
```
- **`label_change()`**: Calls the function to start updating the language labels.
- **`root.mainloop()`**: Enters the Tkinter event loop, waiting for user interaction and keeping the application running.

### Summary
This Tkinter application is structured to provide a user-friendly interface for translating text between different languages using the Google Translate API. It includes features for language selection, input/output text areas, error handling, and dynamic updates of language labels. The layout is designed to be intuitive, making it easy for users to interact with the translator without needing extensive programming knowledge. Each function and UI element is carefully crafted to ensure a seamless experience for the end user.
