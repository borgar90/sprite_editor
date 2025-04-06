class WindowManager:
    def __init__(self):
        self.windows = []

    def open_project_window(self, project_data):
        window = AppWindow(project_data)
        self.windows.append(window)

    def close_window(self, window):
        if window in self.windows:
            window.destroy()
            self.windows.remove(window)
