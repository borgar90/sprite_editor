import os
import tkinter as tk
from PIL import Image, ImageTk
import time


class SplashScreen(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # Remove window decorations and make background transparent
        self.overrideredirect(True)
        self.configure(bg="black")
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", "black")

        # Fullscreen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Create a canvas for animation
        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the logo
        logo_path = os.path.join("assets", "splash", "sprite_logo.png")
        logo_image = Image.open(logo_path).convert("RGBA").resize((400, 120))
        self.logo_image = ImageTk.PhotoImage(logo_image)
        self.logo_id = self.canvas.create_image(screen_width // 2, screen_height // 3, image=self.logo_image, anchor="center")

        # Start animation
        self.start_time = time.perf_counter()
        self._animate()

        # Transition to the next screen after 3 seconds
        self.after(3000, self.cleanup)

    def _animate(self):
        """Handle animation logic."""
        elapsed = (time.perf_counter() - self.start_time) * 1000  # milliseconds

        # Fade-in effect for the logo (0-1000ms)
        if elapsed <= 1000:
            alpha = int(255 * (elapsed / 1000))
            faded = Image.open(os.path.join("assets", "splash", "sprite_logo.png")).convert("RGBA").resize((400, 120))
            faded.putalpha(alpha)
            self.logo_image = ImageTk.PhotoImage(faded)
            self.canvas.itemconfig(self.logo_id, image=self.logo_image)

        # Continue animation loop
        if elapsed < 3000:
            self.after(33, self._animate)  # ~30 FPS

    def cleanup(self):
        """Cleanup and transition to the next screen."""
        self.destroy()
        self.controller.show_frame("ProjectScreen")
