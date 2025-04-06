# app/screens/base_screen.py

import tkinter as tk
from abc import ABC, abstractmethod
from app.gui_elements.gui_element import GUIElement

class Screen(GUIElement):
    def __init__(self, root, app_logic):
        super().__init__(root)
        self.layout = MainEditorLayout(root, app_logic)

    def show(self):
        self.layout.render()

    def hide(self):
        self.layout.unrender()
