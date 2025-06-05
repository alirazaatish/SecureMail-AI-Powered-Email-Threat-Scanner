import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class PhishingDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureMail | AI-Powered Email Threat Scanner")
        self.root.geometry("1000x650")
        self.root.configure(bg="#ffffff")  # white bg

        self.email_content = ""
        self.analysis_result = ()

        self.setup_ui()

    def setup_ui(self):
        # Sidebar Frame
        sidebar = tk.Frame(self.root, bg="#f0f4f8", width=220)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="SecureMail", font=("Segoe UI", 20, "bold"),
                 fg="#2563eb", bg="#f0f4f8").pack(pady=(30, 5))

        tk.Label(sidebar, text="Detect. Defend.\nDeliver Secure Email.",
                 font=("Segoe UI", 11), fg="#475569", bg="#f0f4f8", justify="center").pack(pady=(0, 20))

        # Sidebar Buttons
        self.make_sidebar_btn(sidebar, "📂 Load Email", self.dummy)
        self.make_sidebar_btn(sidebar, "🔍 Analyze Email", self.dummy)
        self.make_sidebar_btn(sidebar, "📄 Generate Report", self.dummy)
        self.make_sidebar_btn(sidebar, "🧹 Clear All", self.dummy)

        # Main Panel Frame
        main_panel = tk.Frame(self.root, bg="#ffffff")
        main_panel.pack(fill="both", expand=True, padx=15, pady=15)

        # Status Bar
        self.status_label = tk.Label(main_panel, text="📄 No file loaded.",
                                     font=("Segoe UI", 11), bg="#ffffff", fg="#475569", anchor="w")
        self.status_label.pack(fill="x", pady=(0, 10))

        # Result Area
        self.result_area = scrolledtext.ScrolledText(main_panel, wrap=tk.WORD,
                                                     font=("Consolas", 11), bg="#f9fafb",
                                                     fg="#1e293b", borderwidth=1, relief="solid",
                                                     insertbackground="#1e293b")
        self.result_area.pack(fill="both", expand=True)

    def make_sidebar_btn(self, parent, text, cmd):
        btn = tk.Button(parent, text=text, command=cmd,
                        font=("Segoe UI", 12, "bold"),
                        bg="#2563eb", fg="white",
                        activebackground="#1e40af",
                        bd=0, relief="flat", height=2)
        btn.pack(fill="x", pady=8, padx=15)
        btn.bind("<Enter>", lambda e: btn.config(bg="#1e40af"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#2563eb"))

    def dummy(self):
        messagebox.showinfo("Info", "This button is not yet connected.")

def main_gui():
    root = tk.Tk()
    app = PhishingDetectorApp(root)
    root.mainloop()
