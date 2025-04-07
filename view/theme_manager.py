"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines ThemeManager, which provides functionality for managing and applying themes to the application.
"""

class ThemeManager:
    """
    Manages application-wide themes and provides methods to apply them to widgets.
    """

    def __init__(self, root):
        self.root = root
        self.current_theme = {
            "background": "#ffffff",
            "foreground": "#000000",
            "button_background": "#0078d7",
            "button_foreground": "#ffffff",
            "label_foreground": "#333333",
        }

    def apply_to_root(self):
        """
        Apply the current theme to the root window.
        """
        self.root.configure(bg=self.current_theme["background"])

    def update_theme(self, new_theme):
        """
        Update the current theme with new values.

        :param new_theme: A dictionary containing theme properties to update.
        """
        self.current_theme.update(new_theme)
        self.apply_to_root()

    def style_widget(self, widget, widget_type):
        """
        Apply the current theme to a specific widget.

        :param widget: The widget to style.
        :param widget_type: The type of the widget (e.g., 'button', 'label').
        """
        if widget_type == "button":
            widget.configure(
                bg=self.current_theme["button_background"],
                fg=self.current_theme["button_foreground"]
            )
        elif widget_type == "label":
            widget.configure(
                fg=self.current_theme["label_foreground"]
            )