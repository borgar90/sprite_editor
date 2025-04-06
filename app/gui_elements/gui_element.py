class GUIElement:
    def __init__(self, root, app_logic=None):
        self.root = root
        self.app_logic = app_logic

    def render(self):
        raise NotImplementedError("Each GUIElement must implement `render` method.")
