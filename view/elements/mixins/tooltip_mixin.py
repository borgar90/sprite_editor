"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This mixin adds tooltip behavior to any Tkinter-based element.
Tooltips appear on hover and disappear on leave or after timeout.
"""

import tkinter as tk
import time


class TooltipMixin:
    """
    A mixin class to add tooltip functionality to widgets.
    Requires the class to have a .widget attribute (Tkinter widget).
    """

    def enable_tooltip(self, text, delay=500):
        """
        Activate tooltip for this widget.

        :param text: Tooltip text content
        :param delay: Delay before showing tooltip (in milliseconds)
        """
        self._tooltip_text = text
        self._tooltip_delay = delay
        self._tooltip_id = None
        self._tooltip_window = None

        self.widget.bind("<Enter>", self._schedule_tooltip)
        self.widget.bind("<Leave>", self._hide_tooltip)

    def _schedule_tooltip(self, event=None):
        self._tooltip_id = self.widget.after(self._tooltip_delay, self._show_tooltip)

    def _show_tooltip(self):
        if self._tooltip_window:
            return

        x = self.widget.winfo_rootx() + 10
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self._tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(
            tw,
            text=self._tooltip_text,
            bg="yellow",
            fg="black",
            relief="solid",
            borderwidth=1,
            font=("Arial", 10)
        )
        label.pack(ipadx=4, ipady=2)

    def _hide_tooltip(self, event=None):
        if self._tooltip_id:
            self.widget.after_cancel(self._tooltip_id)
            self._tooltip_id = None

        if self._tooltip_window:
            self._tooltip_window.destroy()
            self._tooltip_window = None
