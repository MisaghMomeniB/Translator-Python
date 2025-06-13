# 🌐 Translator–Python GUI

A desktop translation tool built with **Python**, featuring a responsive **Tkinter GUI** and powered by the `googletrans` library for fast, multilingual text translation.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Code Structure](#code-structure)  
7. [Potential Enhancements](#potential-enhancements)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## 💡 Overview

This project provides a clean and intuitive **GUI application** for text translation—simply select a source and target language, enter or paste text, and get an instant translation. Perfect for language learners, quick lookups, or desktop usage.

---

## ✅ Features

- 🔍 **Automatic language detection**  
- 🔁 **Bidirectional translation** between any `googletrans`-supported languages :contentReference[oaicite:1]{index=1}  
- 📝 Separate, scrollable text areas for input and output  
- 🎨 Responsive GUI with language dropdowns and translate button  
- ⚠️ **Error handling** with dialog alerts for invalid input or translation errors

---

## 🛠️ Prerequisites

- Python **3.7+**  
- GUI toolkit: **Tkinter** (included with standard Python)  
- Install `googletrans` package (recommended version):

```bash
pip install googletrans==4.0.0-rc1
````

* (Optional) Place assets like `GT.png` & `trns.png` in the same folder for visual enhancement ([github.com][1])

---

## ⚙️ Installation

```bash
git clone https://github.com/MisaghMomeniB/Translator-Python.git
cd Translator-Python/src
```

---

## 🚀 Usage

```bash
python translator_app.py
```

Then:

1. Choose **source language** (or let it auto-detect)
2. Select **target language**
3. Paste or type text in the left panel
4. Press **"Translate"** to view the translation on the right

Features include:

* Auto-updating GUI labels for chosen languages
* Scrollable text boxes for long input/output ([github.com][1], [github.com][2], [github.com][3])

---

## 📁 Code Structure

```
Translator-Python/
├── src/
│   └── translator_app.py     # Core GUI + translation logic
├── assets/                   # Optional: GT.png, trns.png icons
├── LICENSE                   # GPL-3.0 License
└── README.md                 # This file
```

Key implementation details in `translator_app.py`:

* `TranslatorApp` class sets up GUI elements and event loops
* `translate_text()` uses `googletrans` for translation with fallback on errors

---

## 💡 Potential Enhancements

* 📂 Add **Save Translation** feature (e.g., `.txt`, clipboard copy)
* 🌐 Integrate alternative APIs (DeepL, Azure, AWS Translate)
* 🗣️ Support **speech-to-text** and **text-to-speech** for accessibility
* 🧩 Language combos customization and **favorite pairs** UI

---

## 🤝 Contributing

Contributions encouraged! To get started:

1. Fork the repo
2. Create a `feature/…` branch
3. Make your changes with clear comments
4. Open a detailed Pull Request

---

## 📄 License

This project is released under the **GPL-3.0 License**—see `LICENSE` for full terms.
