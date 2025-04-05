# right_panel.py

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import IntVar, BooleanVar

class RightPanel(tb.Frame):
    def __init__(self, parent, app_logic, refresh_preview):
        super().__init__(parent, bootstyle="dark")
        self.pack(fill="both", expand=True)
        self.app_logic = app_logic
        self.refresh_preview = refresh_preview

        # State vars
        self.tile_width = IntVar(value=app_logic.tile_width)
        self.tile_height = IntVar(value=app_logic.tile_height)
        self.lock_tile = BooleanVar(value=True)

        self.slice_start = IntVar(value=app_logic.slice_start)
        self.slice_end = IntVar(value=app_logic.slice_end)

        self.grid_cols = IntVar(value=16)
        self.grid_rows = IntVar(value=16)
        self.lock_grid = BooleanVar(value=True)

        # Build sections
        self._create_collapsible_section("🧱 Tile", self._tile_ui)
        self._create_collapsible_section("🎞 Slice Range", self._slice_ui)
        self._create_collapsible_section("🧮 Painter Grid", self._grid_ui)

    def _create_collapsible_section(self, title, build_content):
        section = tb.Labelframe(self, text=title, bootstyle="info", padding=10)
        section.pack(fill="x", padx=8, pady=6)

        # Collapsible toggle
        toggle_btn = tb.Button(section, text="⯆", width=3, bootstyle="secondary-outline")
        toggle_btn.pack(side="right", anchor="ne", pady=2)
        content = tb.Frame(section)
        content.pack(fill="x", expand=True)

        def toggle():
            if content.winfo_ismapped():
                content.forget()
                toggle_btn.config(text="⯈")
            else:
                content.pack(fill="x", expand=True)
                toggle_btn.config(text="⯆")

        toggle_btn.config(command=toggle)

        build_content(content)

    def _tile_ui(self, parent):
        row = tb.Frame(parent)
        row.pack(fill="x", pady=4)
        tb.Label(row, text="Width:").pack(side=LEFT)
        tb.Entry(row, textvariable=self.tile_width, width=5).pack(side=LEFT, padx=5)
        tb.Label(row, text="Height:").pack(side=LEFT, padx=(10, 0))
        tb.Entry(row, textvariable=self.tile_height, width=5).pack(side=LEFT, padx=5)
        tb.Checkbutton(parent, text="Lock dimensions", variable=self.lock_tile, bootstyle="success-round-toggle").pack(anchor="w", pady=4)

    def _slice_ui(self, parent):
        row = tb.Frame(parent)
        row.pack(fill="x", pady=4)
        tb.Label(row, text="Start:").pack(side=LEFT)
        tb.Entry(row, textvariable=self.slice_start, width=6).pack(side=LEFT, padx=5)
        tb.Label(row, text="End:").pack(side=LEFT, padx=(10, 0))
        tb.Entry(row, textvariable=self.slice_end, width=6).pack(side=LEFT, padx=5)

    def _grid_ui(self, parent):
        row = tb.Frame(parent)
        row.pack(fill="x", pady=4)
        tb.Label(row, text="Cols:").pack(side=LEFT)
        tb.Entry(row, textvariable=self.grid_cols, width=5).pack(side=LEFT, padx=5)
        tb.Label(row, text="Rows:").pack(side=LEFT, padx=(10, 0))
        tb.Entry(row, textvariable=self.grid_rows, width=5).pack(side=LEFT, padx=5)
        tb.Checkbutton(parent, text="Lock grid size", variable=self.lock_grid, bootstyle="info-round-toggle").pack(anchor="w", pady=4)
