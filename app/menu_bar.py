import tkinter as tk
from tkinter import filedialog, messagebox

class MenuBar:
    def __init__(self, root, app_logic, screen_switch_callback):
        self.root = root
        self.app_logic = app_logic
        self.screen_switch_callback = screen_switch_callback  # NEW
        self.menu = tk.Menu(self.root)

        self._build_file_menu()
        self._build_project_menu()
        self._build_edit_menu()
        self._build_view_menu()
        self._build_help_menu()


    def _build_file_menu(self):
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open Image...", command=self.open_image)
        file_menu.add_command(label="Export JSON...", command=self.export_json)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=file_menu)

    def _build_project_menu(self):
        project_menu = tk.Menu(self.menu, tearoff=0)
        project_menu.add_command(label="New Project", command=self.new_project_callback)
        project_menu.add_command(label="Open Project", command=self.open_project_callback)
        project_menu.add_command(label="Save Project", command=self.save_project_callback)
        project_menu.add_command(label="Close Project", command=self.close_project_callback)
        self.menu.add_cascade(label="Project", menu=project_menu)

    def _build_edit_menu(self):
        edit_menu = tk.Menu(self.menu, tearoff=0)
        edit_menu.add_command(label="Undo", state="disabled")
        edit_menu.add_command(label="Redo", state="disabled")
        self.menu.add_cascade(label="Edit", menu=edit_menu)

    def _build_view_menu(self):
        view_menu = tk.Menu(self.menu, tearoff=0)
        view_menu.add_command(label="Switch to Painter", command=lambda: self.screen_switch_callback("paint"))
        view_menu.add_command(label="Switch to Preview", command=lambda: self.screen_switch_callback("preview"))
        self.menu.add_cascade(label="View", menu=view_menu)

    def _build_help_menu(self):
        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.menu.add_cascade(label="Help", menu=help_menu)

    # --- Menu Commands ---

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if path:
            messagebox.showinfo("Selected", f"You selected:\n{path}")
            self.app_logic.load_image(path)

    def export_json(self):
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if path:
            messagebox.showinfo("Export", f"Export path:\n{path}")
            # TODO: call self.app_logic.export_json(path)

    def reload_preview(self):
        messagebox.showinfo("Preview", "Reloading preview...")
        # TODO: trigger canvas repaint

    def show_about(self):
        messagebox.showinfo("About", "SpriteToJSON GUI\nCreated by God with ChatGPT.")


    def new_project_callback(self):
       self.app_logic.new_project()

    def open_project_callback(self):
        self.app_logic.open_project()

    def save_project_callback(self):
        self.app_logic.save_project()

    def close_project_callback(self):
        self.app_logic.close_project()
