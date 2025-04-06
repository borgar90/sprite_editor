import tkinter as tk

class AppWindow:
    def __init__(self, project_data):
        self.root = tk.Toplevel()
        self.app_logic = AppLogic()
        self.screen_manager = ScreenManager(self.root, self.app_logic)
        self.gui = GUIManager(self.root, self.app_logic, self.screen_manager)

        # Maybe:
        self.root.title(f"Project: {project_data['name']}")
        self.screen_manager.load_screen("default")

    def destroy(self):
        self.root.destroy()
