# app/interceptors/save_warning_interceptor.py
from tkinter import messagebox
from interceptor import Interceptor

class SaveWarningInterceptor(Interceptor):
    def before_close(self, file_id, file_data) -> bool:
        if file_data.get("dirty"):
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                f"Do you want to save changes to '{file_data['name']}' before closing?"
            )
            if response is None:  # Cancel
                return False
            elif response:  # Yes
                if file_data.get("on_save"):
                    file_data["on_save"]()
        return True