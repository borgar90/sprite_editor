"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines ProjectTileElement, a reusable GUI element representing a selectable project tile.
Each tile displays a preview image and title, and emits a callback when selected.
"""

import tkinter as tk
from PIL import Image, ImageTk
from view.elements.base_element import BaseElement


class ProjectTileElement(BaseElement):
    """
    A clickable project tile displaying a thumbnail and title.
    Calls a provided callback when selected.
    """

    def __init__(self, master, title, img_path, data, on_select, **kwargs):
        """
        Initialize the project tile.

        :param master: Parent container
        :param title: Project title
        :param img_path: Path to preview image
        :param data: Arbitrary data payload (e.g. project info)
        :param on_select: Callback when tile is selected
        :param kwargs: Optional styling overrides
        """
        super().__init__(master, **kwargs)
        self.title = title
        self.img_path = img_path
        self.data = data
        self.on_select = on_select
        self.selected = False
        self.photo = None

    def render(self, master=None):
        if master:
            self.master = master

        self.widget = tk.Frame(self.master, bg="#2e2e2e", bd=2, relief="solid")
        self.widget.pack(padx=20, pady=10, fill="x")

        img = Image.open(self.img_path).resize((100, 100))
        self.photo = ImageTk.PhotoImage(img)
        label_img = tk.Label(self.widget, image=self.photo, bg="#2e2e2e")
        label_img.image = self.photo
        label_img.pack(side="left", padx=10, pady=10)

        label_title = tk.Label(
            self.widget, text=self.title, fg="white", bg="#2e2e2e", font=("Arial", 14)
        )
        label_title.pack(side="left", padx=10)

        # Bind click for entire frame and content
        for widget in (self.widget, label_img, label_title):
            widget.bind("<Button-1>", lambda e: self.select())

    def select(self):
        """
        Mark this tile as selected and notify callback.
        """
        self.set_selected(True)
        if self.on_select:
            self.on_select(self)

    def set_selected(self, value: bool):
        """
        Update selection state and visual border.
        """
        self.selected = value
        self.widget.config(highlightthickness=3 if value else 2,
                           highlightbackground="#00ffe0" if value else "#2e2e2e")
