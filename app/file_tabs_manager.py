# app/file_tabs_manager.py
import tkinter as tk
from tkinter import ttk, messagebox
from files.stj_file import STJFile

from files.file_registry import  FileRegistry  # Import the registry

class FileTabsManager:
    def __init__(self, root, on_close_callback=None):
        self.root = root
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="x", side="top")
        self.tabs = {}
        self.on_close_callback = on_close_callback
        self.notebook.bind("<Button-1>", self._on_tab_click)
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_switched)
        self.on_switch_callback = None
        self._add_plus_tab()

    def _add_plus_tab(self):
        plus_tab = ttk.Frame(self.notebook)
        self.notebook.add(plus_tab, text="+")
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    def _on_tab_changed(self, event):
        if self.notebook.index("current") == self.notebook.index("end") - 1:
            self.add_new_tab()

    def add_new_tab(self, filepath=None):
        file_instance = FileRegistry.create_new(filepath)
        self._add_tab_with_close(file_instance)

    def _add_tab_with_close(self, file_instance):
        tab = ttk.Frame(self.notebook)
        display_name = " " + file_instance.filename + "  ⨉"
        self.notebook.insert("end-1", tab, text=display_name)
        self.tabs[file_instance.filename] = {"frame": tab, "file": file_instance}
        self.notebook.select(tab)

    def _on_tab_click(self, event):
        # Detect click near right end of tab label (simulate ⨉ area)
        clicked_index = self.notebook.index(f"@{event.x},{event.y}")
        if clicked_index >= self.notebook.index("end") - 1:
            return  # Ignore "+" tab

        tab_id = self.notebook.tabs()[clicked_index]
        tab_text = self.notebook.tab(tab_id, "text")

        if tab_text.endswith("⨉"):
            # Roughly assume ⨉ was clicked if click is far right in the tab
            tab_bbox = self.notebook.bbox(clicked_index)
            if tab_bbox and event.x >= tab_bbox[0] + tab_bbox[2] - 24:  # 24px from right
                filename = tab_text.strip()[0:-1].strip()
                self._attempt_close_tab(filename)

    def _attempt_close_tab(self, filename):
        file_entry = self.tabs.get(filename)
        if not file_entry:
            return

        file = file_entry["file"]
        frame = file_entry["frame"]

        if file.has_unsaved_changes():
            from tkinter import messagebox
            result = messagebox.askyesnocancel("Unsaved Changes",
                                               f"{file.filename} has unsaved changes.\nDo you want to save before closing?")
            if result is None:
                return  # Cancel
            elif result:
                file.save()

        # Remove tab
        self.notebook.forget(frame)
        del self.tabs[filename]
        if self.on_close_callback:
            self.on_close_callback(filename)

    def _on_tab_switched(self, event):
        current_index = self.notebook.index("current")
        if current_index == self.notebook.index("end") - 1:
            self.add_new_tab()
            return

        selected_tab = self.notebook.select()

        for filename, info in self.tabs.items():
            if self.notebook.index(info["frame"]) == current_index:
                self._highlight_tab(info["frame"])
                if hasattr(self, 'on_switch_callback') and callable(self.on_switch_callback):
                    self.on_switch_callback(filename)
                break

    def _highlight_tab(self, tab):
        # Simple glow pulse effect — requires ttk style setup or tk widget color shift
        def pulse(count=0):
            if count > 10:
                self.notebook.tab(tab, background="#3a3a3a")  # Reset
                return
            color = "#4e9a06" if count % 2 == 0 else "#3a3a3a"
            self.notebook.tab(tab, background=color)
            tab.after(80, lambda: pulse(count + 1))

        pulse()

    def set_on_switch_callback(self, callback):
        self.on_switch_callback = callback
