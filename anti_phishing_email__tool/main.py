# File: main.py
import tkinter as tk
from ui.gui import PhishingDetectorApp

if __name__ == '__main__':
    root = tk.Tk()
    app = PhishingDetectorApp(root)
    root.mainloop()