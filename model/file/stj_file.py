# Moved from files/stj_file.py
import os
import json
from base_file import BaseFile

class STJFile(BaseFile):
    def __init__(self, filename, path):
        super().__init__(filename, path)

    def save(self):
        """Saves the current data to a .stj file in JSON format."""
        full_path = os.path.join(self.path, self.filename)
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)
        self.mark_saved()
        print(f"[STJFile] Saved: {full_path}")

    def load(self):
        """Loads data from a .stj file."""
        full_path = os.path.join(self.path, self.filename)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            self.mark_saved()
            print(f"[STJFile] Loaded: {full_path}")
        else:
            print(f"[STJFile] File does not exist: {full_path}")