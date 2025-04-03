import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter"], "include_files": []}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name = "HTML Signature Generator",
    version = "0.0.1",
    description = "A simple application to generate HTML email signatures. Developed by Salman Sakib © 2025",
    options = {"build_exe": build_exe_options},
    executables = [Executable("signature_maker.py", base=base, icon="signature.ico")],
)
