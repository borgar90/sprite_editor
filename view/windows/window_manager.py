import tkinter as tk
from view.screens.screen_manager import ScreenManager


class WindowManager:
    def __init__(self, root):
        self.root = root
        self.windows = {}  # A dictionary to hold all windows
        self.active_window = None

    def create_window(self, window_name):
        """
        Create a new window with its own screen manager and register it.
        """
        if window_name not in self.windows:
            window = tk.Toplevel(self.root)
            window.attributes("-fullscreen", True)  # or other configuration for the window
            window.configure(bg="black")  # Customize background as needed
            window.screen_manager = ScreenManager(window)
            self.windows[window_name] = window
            self.active_window = window
        else:
            self.active_window = self.windows[window_name]

        return self.active_window

    def show_window(self, window_name):
        """
        Show the specified window.
        """
        window = self.windows.get(window_name)
        if window:
            window.deiconify()  # Make sure the window is shown
            self.active_window = window

    def hide_window(self, window_name):
        """
        Hide the specified window.
        """
        window = self.windows.get(window_name)
        if window:
            window.withdraw()
