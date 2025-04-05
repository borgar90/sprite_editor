import tkinter as tk
from tkinter import filedialog
from app.widgets import (
    create_label,
    create_button,
    create_entry,
    create_combobox,
    create_separator,
)

class ToolsPanel:
    def __init__(self, parent_frame, app_logic, refresh_preview_callback):
        self.frame = tk.Frame(parent_frame, bg="#1e1e2e")
        self.frame.pack(fill="y", expand=True, padx=5, pady=5)

        self.app_logic = app_logic
        self.refresh_preview = refresh_preview_callback

        self._build_controls()

    def _build_controls(self):
        create_label(self.frame, text="Mode:").pack(anchor="w", pady=(5, 0))
        self.mode_var = tk.StringVar(value=self.app_logic.mode)
        mode_menu = create_combobox(self.frame, values=["atlas", "tiledmap"], variable=self.mode_var)
        mode_menu.pack(fill="x")
        mode_menu.bind("<<ComboboxSelected>>", lambda e: self._update_mode(self.mode_var.get()))

        create_label(self.frame, text="Tile Width:").pack(anchor="w", pady=(10, 0))
        self.tile_width_entry = create_entry(self.frame)
        self.tile_width_entry.insert(0, str(self.app_logic.tile_width))
        self.tile_width_entry.pack(fill="x")

        create_label(self.frame, text="Tile Height:").pack(anchor="w", pady=(10, 0))
        self.tile_height_entry = create_entry(self.frame)
        self.tile_height_entry.insert(0, str(self.app_logic.tile_height))
        self.tile_height_entry.pack(fill="x")

        create_label(self.frame, text="Slice Start:").pack(anchor="w", pady=(10, 0))
        self.slice_start_entry = create_entry(self.frame)
        self.slice_start_entry.insert(0, str(self.app_logic.slice_start))
        self.slice_start_entry.pack(fill="x")

        create_label(self.frame, text="Slice End:").pack(anchor="w", pady=(10, 0))
        self.slice_end_entry = create_entry(self.frame)
        self.slice_end_entry.insert(0, str(self.app_logic.slice_end))
        self.slice_end_entry.pack(fill="x")

        create_separator(self.frame).pack(fill="x", pady=10)

        create_button(self.frame, text="🎬 Preview", command=self._on_preview).pack(fill="x", pady=5)
        create_button(self.frame, text="💾 Export JSON", command=self._on_export).pack(fill="x", pady=5)

    def _update_mode(self, new_mode):
        self.app_logic.mode = new_mode
        self.refresh_preview()

    def _on_preview(self):
        self._sync_values_to_logic()
        if self.app_logic.image:
            self.app_logic.on_image_loaded(self.app_logic.image)
        else:
            self.app_logic.request_preview()

    def _on_export(self):
        self._sync_values_to_logic()
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if path:
            self.app_logic.export_json(path)

    def _sync_values_to_logic(self):
        try:
            self.app_logic.tile_width = int(self.tile_width_entry.get())
            self.app_logic.tile_height = int(self.tile_height_entry.get())
            self.app_logic.slice_start = int(self.slice_start_entry.get())
            self.app_logic.slice_end = int(self.slice_end_entry.get())
        except ValueError:
            print("[ToolsPanel] Invalid input values.")
