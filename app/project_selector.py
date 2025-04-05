# app/project_selector.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class ProjectSelector:
    def __init__(self, root, on_project_selected):
        self.root = root
        self.on_project_selected = on_project_selected
        self.base_path = os.path.expanduser('~')
        self.name_entry = tk.StringVar()

        self.popup = tk.Toplevel(root)
        self.popup.title("Velg prosjekt")
        self.popup.configure(bg="#1e1e2e")
        self.popup.resizable(False, False)

        self._center_popup(width=420, height=280)

        # Logo
        logo_img = Image.open("assets/splash/sprite_logo.png").resize((220, 66))
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(self.popup, image=logo_tk, bg="#1e1e2e")
        logo_label.image = logo_tk
        logo_label.pack(pady=(20, 10))

        # Tittel
        tk.Label(
            self.popup,
            text="Velg prosjekt",
            fg="white",
            bg="#1e1e2e",
            font=("Arial", 14, "bold")
        ).pack(pady=(0, 10))

        # Knapper
        tk.Button(self.popup, text="📁 Åpne eksisterende prosjekt", command=self.open_project).pack(pady=5)
        tk.Button(self.popup, text="🆕 Start nytt prosjekt", command=self.new_project).pack(pady=5)

        self.popup.transient(root)
        self.popup.grab_set()
        self.popup.focus_force()

    def _center_popup(self, width, height):
        self.popup.update_idletasks()
        screen_w = self.popup.winfo_screenwidth()
        screen_h = self.popup.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.popup.geometry(f"{width}x{height}+{x}+{y}")

    def open_project(self):
        path = filedialog.askdirectory(title="Velg prosjektmappe")
        if path:
            print("[ProjectSelector] Åpner prosjekt:", path)
            self.popup.destroy()
            self.on_project_selected({"path": path, "type": "existing"})

    def new_project(self):
        self.base_path = filedialog.askdirectory(title="Velg mappe for nytt prosjekt")
        if not self.base_path:
            return
        self.input_name()

    def submit_name(self):
            name = self.name_entry.get().strip()
            if not name:
                messagebox.showerror("Feil", "Du må oppgi et prosjektnavn.")
                return

            print("[ProjectSelector] Nytt prosjekt:", self.base_path, name)
            self.name_popup.destroy()
            self.popup.destroy()
            self.on_project_selected({
                "path": self.base_path,
                "name": name,
                "type": "new"
            })

    def input_name(self):
        # --- Ny popup for prosjektnavn ---
        self.name_popup = tk.Toplevel(self.root)
        self.name_popup.title("Prosjektnavn")
        self.name_popup.configure(bg="#1e1e2e")
        self.name_popup.resizable(False, False)

        # Midtstill popup
        self.name_popup.update_idletasks()
        width, height = 360, 140
        x = (self.name_popup.winfo_screenwidth() - width) // 2
        y = (self.name_popup.winfo_screenheight() - height) // 2
        self.name_popup.geometry(f"{width}x{height}+{x}+{y}")

        tk.Label(self.name_popup, text="Navn på prosjekt:", bg="#1e1e2e", fg="white", font=("Arial", 12)).pack(pady=(20, 5))
        tk.Entry(self.name_popup, textvariable=self.name_entry, font=("Arial", 12), width=28).pack(pady=5)


        tk.Button(self.name_popup, text="Opprett", command=self.submit_name).pack(pady=(10, 5))

        self.name_popup.transient(self.root)
        self.name_popup.grab_set()


