"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This mixin adds popover functionality to any element that has a .widget attribute.
Popover content is provided by a builder function and is shown on click.
"""

import tkinter as tk


class PopoverMixin:
    """
    A mixin to add click-activated popovers to GUI elements.
    Each popover is a transient Toplevel window with dynamic content.
    """

    def enable_popover(self, content_builder):
        """
        Enable popover support.

        :param content_builder: Function that receives a popup window and populates its content
        """
        self._popover_builder = content_builder
        self._popover_window = None
        self.widget.bind("<Button-1>", self._toggle_popover)

    def _toggle_popover(self, event=None):
        if self._popover_window:
            self._hide_popover()
        else:
            self._show_popover()

    def _show_popover(self):
        if not hasattr(self, "widget") or not self._popover_builder:
            return

        x = self.widget.winfo_rootx()
        y = self.widget.winfo_rooty() + self.widget.winfo_height()

        self._popover_window = pop = tk.Toplevel(self.widget)
        pop.wm_overrideredirect(True)
        pop.wm_geometry(f"+{x}+{y}")
        pop.configure(bg="#2e2e2e")

        self._popover_builder(pop)

        # Hide when clicked outside
        pop.bind("<FocusOut>", lambda e: self._hide_popover())
        pop.focus_set()

    def _hide_popover(self):
        if self._popover_window:
            self._popover_window.destroy()
            self._popover_window = None