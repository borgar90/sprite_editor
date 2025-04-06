# files/base_file.py
import hashlib
import json
from abc import ABC, abstractmethod

class BaseFile(ABC):
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.data = {}
        self._last_saved_hash = self._calculate_hash()

    def _calculate_hash(self):
        """Serialize and hash the current data dictionary for change tracking."""
        serialized = json.dumps(self.data, sort_keys=True)
        return hashlib.md5(serialized.encode("utf-8")).hexdigest()

    def has_unsaved_changes(self):
        """Check if file content has changed since last save."""
        return self._calculate_hash() != self._last_saved_hash

    def mark_saved(self):
        """Call this after successfully saving."""
        self._last_saved_hash = self._calculate_hash()

    @abstractmethod
    def save(self):
        """Must be implemented to save this file type."""
        pass

    @abstractmethod
    def load(self):
        """Must be implemented to load this file type."""
        pass
