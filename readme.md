# PGCD Finder Project 

## Overview 

PGCD Finder is a Python application designed to help users calculate the Greatest Common Divisor (GCD) of two polynomials. The tool is user-friendly, visually appealing, and suitable for students, teachers, and anyone working with polynomial mathematics.

## Features 

- **Polynomial GCD Calculation:** Quickly compute the GCD of two polynomials.
- **User-Friendly Interface:** Modern and intuitive GUI built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter).
- **Keyboard Support:** On-screen keyboard for easy polynomial entry ⌨️.
- **Input Validation:** Automatic correction and validation of polynomial input 🧹.
- **Auto-Correction Toggle:** Enable or disable automatic input correction for polynomials in the settings ⚙️.
- **Tips & Examples:** Built-in tips and example polynomials to help users get started 💡📚.
- **Theme Support:** Switch between dark, light, and system appearance modes 🌗.
- **Clear Results Display:** Shows quotient, remainder, and GCD in a readable format 📝.
- **Improved Floating-Point Handling:** Floating-point coefficients are now correctly parsed and displayed.
- **History Feature:** View, restore, copy, and clear your calculation history 🕑.

## What's New & Updates 🆕

- **Settings Window:**  
  A dedicated settings window allows you to:
  - Toggle auto-correction for polynomial input (ON/OFF).
  - Instantly switch between light, dark, and system appearance modes.
  - All settings changes are applied live to the application.

- **Input Validation System Improvements:**  
  - Supports input like `X3` which is auto-converted to `X³` (superscript).
  - Improved handling and formatting of floating-point coefficients (e.g., `2.500` becomes `2.5`, `3.00` becomes `3`).
  - You can disable auto-correction for manual input; if disabled, polynomials must be entered in the correct format.

- **Tips Window Redesign:**  
  - Tips and instructions are now visually separated:
    - **Authorized actions** are shown with green color and a ✅ icon.
    - **Warnings and restrictions** are shown with yellow/orange color and a ⚠️ icon.
  
- **History Feature:**  
  - A new **History** window is available from the toolbar.
  - **View all previous calculations** with polynomials and their GCD.
  - **Restore** any previous calculation by clicking the "Show" button.
  - **Copy** the result to the clipboard with one click.
  - **Clear** the entire history using the delete button.

## Usage 🛠️

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/Mohamed2006-Dev/POLYNOME-PGCD-FINDER.git
   cd POLYNOME-PGCD-FINDER
   ```

2. **Install Dependencies**
   Make sure you have Python 3.x installed. Install required packages:
   ```bash
   pip install customtkinter sympy pillow
   ```

3. **Run the Application**
   ```bash
   python Start.py
   ```

4. **How to Use**
   - Enter two polynomials in the input fields (e.g., `X**2 + 2*X + 1` and `X + 1`).
   - Use the on-screen keyboard or your physical keyboard.
   - Click the main button to calculate the GCD.
   - View the quotient, remainder, and GCD in the results section.
   - Use the "Tips" and "Example" buttons for guidance.
   - **Auto-Correction:** You can enable or disable auto-correction in the settings window. If disabled, make sure to enter polynomials in the correct format to avoid errors.
   - **History:** Access the history window from the toolbar to view, restore, copy, or clear your previous calculations.

## Dependencies 📦

- [Python 3.x](https://www.python.org/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [sympy](https://www.sympy.org/)
- [Pillow (PIL)](https://python-pillow.org/)

## Project Structure 🗂️

- `Start.py` - Application entry point.
- `Management/ProjectManager.py` - Main controller logic.
- `ExtraFrames/` - GUI components (Entry, Result, Keyboard, Footer, etc.).
- `utils/` - Utility modules for parsing, calculation, and helpers.
- `theme/` - Color and style definitions.
- `config/assets.py` - Image asset loader.
- `res/` - Image resources.

## Acknowledgements

- Built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern Python GUI.
- Uses [sympy](https://www.sympy.org/) for symbolic mathematics.

---

Enjoy using PGCD Finder! If you have suggestions or find bugs, feel free to open an issue or contribute. 😊

