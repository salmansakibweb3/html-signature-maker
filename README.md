# 📬 HTML Signature Generator

A simple and customizable Python GUI application to generate professional HTML email signature blocks. Built using `Tkinter`, this tool allows you to input personal details and export a clean, mobile-friendly signature in just seconds.

---

## ✨ Features

- Simple GUI with fields for Name, Title, Phone, Email, LinkedIn, and Profile Picture
- Automatically formats the phone number for tap-to-call functionality
- Clean HTML export that works in Outlook, Gmail, Apple Mail, etc.
- Usage tracking lock (optional, can be disabled or modified)
- Option to compile into a portable Windows `.exe`

---

## 📁 Folder Structure

```
application/
├── signature_maker.py
├── setup.py
├── signature.ico (optional - app icon)
├── requirements.txt
└── .hidden_usage_data (auto-created)
```

---

## 🛠 Requirements

This project uses **Python 3.10+** and the following built-in libraries:

- `tkinter` (for GUI)
- `os`, `base64`, `re` (for logic and validation)

You will also need:
- `cx_Freeze` for building `.exe` (optional)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/html-signature-generator.git
cd html-signature-generator/application
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> 📝 `tkinter` comes bundled with Python. If you’re on Linux and it’s missing:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🖥 Running the App

To launch the signature generator:

```bash
python signature_maker.py
```

You’ll see a simple GUI window with input fields for Name, Title, Phone, Email, Profile Picture, and LinkedIn URL.

---

## 📦 Build a Windows Executable (Optional)

### Add an `.ico` file (optional)

Place your icon in the same directory and update `setup.py` like this:

```python
Executable("signature_maker.py", base=base, icon="signature.ico")
```

### Build the `.exe` file

```bash
python setup.py build
```

You’ll find your `.exe` inside:

```
application/build/exe.win-amd64-3.12/
```

💡 **To distribute**: zip that entire folder and share it.

---

## 🔓 Reset Usage Lock (Optional)

The app tracks usage in a file called `.hidden_usage_data`.

To reset the limit:

```bash
del .hidden_usage_data
```

Or use this inside Python:

```python
import os
if os.path.exists(".hidden_usage_data"):
    os.remove(".hidden_usage_data")
```

---

## 📦 Optional: Build a Single Executable File (Advanced)

Install PyInstaller (alternative to cx_Freeze):

```bash
pip install pyinstaller
```

Then build with:

```bash
pyinstaller --noconsole --onefile --icon=signature.ico signature_maker.py
```

Your portable `.exe` will be in the `dist/` folder.

---

## 📄 License

MIT License © 2025 Salman Sakib
