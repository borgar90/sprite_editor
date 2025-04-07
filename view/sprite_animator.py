"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines SpriteAnimator, which handles sprite animation on a canvas.
"""

import os
from PIL import Image, ImageTk

class SpriteAnimator:
    """
    Handles sprite animation on a canvas.
    """

    def __init__(self, canvas, sprite_dir, x, y):
        self.canvas = canvas
        self.sprite_dir = sprite_dir
        self.x = x
        self.y = y
        self.frames = []
        self.current = 0
        self.sprite_id = None

        self._load_frames()

    def _load_frames(self):
        """Loads sprite frames from the specified directory."""
        files = sorted([f for f in os.listdir(self.sprite_dir) if f.endswith('.png')])
        for file in files:
            path = os.path.join(self.sprite_dir, file)
            img = Image.open(path)
            tk_img = ImageTk.PhotoImage(img)
            self.frames.append(tk_img)

    def start(self, interval=40):
        """Starts the sprite animation."""
        if not self.frames:
            return
        if self.sprite_id is None:
            self.sprite_id = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.frames[0])
        self._animate(interval)

    def _animate(self, interval):
        """Animates the sprite frames."""
        self.canvas.itemconfig(self.sprite_id, image=self.frames[self.current])
        self.current = (self.current + 1) % len(self.frames)
        self.canvas.after(interval, lambda: self._animate(interval))