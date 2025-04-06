# files/file_registry.py
import os
from files.stj_file import STJFile
# Future file types:
# from files.png_file import PNGFile
# from files.stjproj_file import STJProjFile


class FileRegistry:
    """
    Factory and resolver for file types based on extension or folder logic.
    """

    @staticmethod
    def open(path: str):
        """
        Detects file type and returns appropriate file handler object.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        _, ext = os.path.splitext(path.lower())

        if ext == ".stj":
            file = STJFile(path)
            file.load()
            return file

        # elif ext == ".png":
        #     return PNGFile(path)

        # elif ext == ".stjproj":
        #     return STJProjFile(path)

        else:
            raise ValueError(f"Unsupported file type: {ext}")

    @staticmethod
    def create_new(path: str):
        """
        Creates and returns a blank file based on path extension.
        """
        _, ext = os.path.splitext(path.lower())

        if ext == ".stj":
            return STJFile(path, data={})

        # elif ext == ".stjproj":
        #     return STJProjFile(path, config={})

        raise ValueError(f"Cannot create unknown file type: {ext}")
