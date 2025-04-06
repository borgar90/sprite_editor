# app_state.py (or inside the controller.py)
class AppState:
    def __init__(self):
        self.state = "splash"  # initial state
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def notify(self):
        for listener in self.listeners:
            listener(self.state)

    def set_state(self, new_state):
        self.state = new_state
        self.notify()  # Notify listeners about the state change
