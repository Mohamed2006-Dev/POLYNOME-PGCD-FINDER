# PGCD Finder 🧮

A graphical Python application to calculate the Greatest Common Divisor (PGCD) of two polynomials using a custom Tkinter-based interface.

## 📌 Overview

This application allows users to input two polynomials \( A(X) \) and \( B(X) \), and it calculates:

- The Quotient
- The Remainder
- The PGCD (GCD) of the polynomials

It includes:
- A virtual keyboard for mathematical symbols
- Real-time input validation
- A tips/help section
- A clean, frame-separated architecture

## 🧠 Built With

- *Python 3.10+*
- *Tkinter*
- *CustomTkinter*
- *SymPy* (used under-the-hood for symbolic calculations)

## 📁 Project Structure

```text
VERSION 2/
├── config/
│   └── assets.py              # Image paths and conversion utilities
├── assets.py                 # Assets management
├── Exceptions/
│   └── Expression.py          # Custom exception handling
├── theme/
|   ├── font.py      # Ctk fonts classes
|   ├── color.py     # Row hexa values of colors
|   └── style.py     # Row values of fonts
├── ExtraFrames/
│   ├── App.py
│   ├── EntryFrame.py
│   ├── FooterFrame.py
│   ├── KeyboardFrame.py
│   ├── ResultFrame.py
│   ├── TipsWindow.py
│   └── TopFrame.py
├── Management/
│   └── ProjectManager.py      # Main logic controller (see below)
├── res/                       # Resource images
├── utils/
│   ├── ButtonsCommands.py     # Custom command bindings
│   ├── Calculator.py          # PGCD algorithm implementation
│   ├── ExtraMethods.py        # Utility methods
│   └── parser.py              # Input extraction and validation
├── Start.py                   # App launcher
```
## 🚀 How to Run

1. Install Python (version must support tkinter and customtkinter modules).


2. Install dependencies (optional, if not installed):

```bash
pip install sympy customtkinter
```

3. Run the app:

```bash
python Start.py
```
No external compilation is required. Just run the script and the GUI will appear.

## 🎨 Features

Modular frame-based GUI

Unicode-to-symbol parser for input processing

Clean separation of logic, interface, and commands

Interactive buttons for tips/help/examples

Images and icons managed dynamically via assets.py

## 📷 Screenshots

(Soon)

## 💳 Credits

All icons used in this project are provided by [Flaticon](https://www.flaticon.com)

## ©️ License

This project is free to use with **no restrictions**

note that this can be change in the futur

## 📢 Update Announcement

1- Adding custom theme to the application

2- Handling the keys of the keyboard

3- Resizing the widgets and texts of the window

## 💡 Future Improvements

Add support for polynomial plotting

Export results to PDF or LaTeX

Enhance accessibility and localization


## 👨‍💻 Author

Developed by a passionate programmer with a focus on clean code architecture and advanced mathematics.
