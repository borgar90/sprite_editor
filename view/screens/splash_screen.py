import os
import tkinter as tk
from PIL import Image, ImageTk
from view.screens.base_screen import BaseScreen
import time


class SplashScreen(BaseScreen):
    """
    Animated splash screen shown on application launch.
    Displays logo and character sprite with running and jumping animation.
    """

    def __init__(self, app_context, root):
        super().__init__(app_context)

        # Initialize Toplevel for splash window (this creates the window)
        self.window = tk.Toplevel(root)
        self.window.attributes("-fullscreen", True)  # Fullscreen mode
        self.window.configure(bg="black")           # Background color (transparent in final view)
        self.window.overrideredirect(True)          # Remove window decorations (like borders)
        self.window.attributes("-topmost", True)    # Keep splash on top
        self.window.attributes("-transparentcolor", "black")  # Set transparency for black color

        # Create a frame inside the Toplevel window for animation handling
        self.frame = tk.Frame(self.window, bg="black")
        self.frame.pack(fill="both", expand=True)

        self._callback = None              # Function to call after splash
        self._frame_index = 0              # Index of current animation frame
        self._frames = []                  # List of loaded ImageTk frames
        self._jump_frames = []             # List of jump frames
        self._char_x = -256                # Starting X position for character
        self._logo_y = None                # Logo Y position (to be set)
        self._char_y = None                # Character Y position (set relative to logo)
        self._canvas = None                # Canvas for displaying animation
        self._logo_img_raw = None          # Logo image for fade-in effect
        self._logo_img_tk = None           # Tkinter compatible logo image
        self.start_time = time.perf_counter()

        # Create a canvas on the frame for drawing the splash
        self._canvas = tk.Canvas(self.frame, bg="black", bd=0, highlightthickness=0)
        self._canvas.pack(fill="both", expand=True)

        # Run the splash screen animation
        self._initialize_animation()

    def _initialize_animation(self):
        """
        Initialize animation setup, including logo and character frames.
        """
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Logo data
        self._logo_img_raw = Image.open("assets/splash/sprite_logo.png").convert("RGBA").resize((400, 120))
        self._logo_img_tk = ImageTk.PhotoImage(self._logo_img_raw)
        self._logo_y = screen_height // 3  # Logo will be placed 1/3rd of the height
        self._logo_id = self._canvas.create_image(screen_width // 2, self._logo_y, image=self._logo_img_tk, anchor="center")

        # Character Y position (100 pixels below the logo)
        self._char_y = self._logo_y + 100

        # Load animation frames
        self._frames = self._load_frames("assets/splash/running")
        self._jump_frames = self._load_frames("assets/splash/jump_loop")

        # Start the animation loop using after on the frame widget (which has after())
        self.frame.after(10, self._start_animation)

        # Schedule callback after 5 seconds
        self.frame.after(5000, self._on_done)

    def schedule_complete_callback(self, callback):
        """
        Set the callback to call after the splash screen finishes.

        :param callback: Function to call when splash screen finishes
        """
        self._callback = callback

    def _on_done(self):
        """
        Called after splash finishes — triggers registered callback and hides splash.
        """
        self.window.withdraw()  # Hide the splash screen window
        self.app_context.app_state.set_state("project")

        if self._callback:
            self._callback()  # Proceed with callback (transition to the next screen)

    def _load_frames(self, folder):
        """
        Load frames for character animation (running, jumping).

        :param folder: Path to folder containing the frames
        """
        frames = []
        files = sorted(
            [f for f in os.listdir(folder) if f.endswith(".png")],
            key=lambda name: int(name.replace(".png", ""))
        )
        for file in files:
            path = os.path.join(folder, file)
            img = Image.open(path).resize((256, 256))
            frames.append(ImageTk.PhotoImage(img))
        return frames

    def _start_animation(self):
        """
        Begin the animation sequence, looping the character frames.
        """
        self._character_id = self._canvas.create_image(
            self._char_x, self._char_y, image=self._frames[0], anchor="nw"
        )
        self._animate_loop()

    def _animate_loop(self):
        """
        Update sprite position, play running and jumping animation in loop.
        """
        elapsed = (time.perf_counter() - self.start_time) * 1000  # milliseconds

        # --- Fade logo (0-1000ms)
        if elapsed <= 1000:
            alpha = int(255 * (elapsed / 1000))
            faded = self._logo_img_raw.copy()
            faded.putalpha(alpha)
            self._logo_img_tk = ImageTk.PhotoImage(faded)
            self._canvas.itemconfig(self._logo_id, image=self._logo_img_tk)

        # --- Run character (0–2000ms)
        if elapsed <= 2000:
            center_target = self.window.winfo_screenwidth() // 2 - 128  # center the character
            percent = min(elapsed / 2000, 1)
            new_x = int(-256 + (center_target + 256) * percent)
            self._char_x = new_x  # Update the current position

            self._canvas.coords(self._character_id, self._char_x, self._char_y)
            self._next_run_frame()

        # --- End run, begin jump
        if elapsed >= 2000 and not hasattr(self, "_jump_started"):
            self._jump_started = True
            self.frame.after(100, self._jump_finish)

        # Continue animation loop
        if elapsed < 3200:
            self.frame.after(33, self._animate_loop)  # ~30 FPS

    def _next_run_frame(self):
        """
        Move to the next frame in the running animation sequence.
        """
        self._frame_index = (self._frame_index + 1) % len(self._frames)
        self._canvas.itemconfig(self._character_id, image=self._frames[self._frame_index])

    def _jump_finish(self):
        """
        Begin the jumping animation after running is complete.
        """
        self.jump_index = 0
        self.jumps_remaining = 4
        self.jump_height = 60
        self.going_up = True
        self.jump_direction = -1
        self.jump_offset = 10

        self._do_jump_frame()

    def _do_jump_frame(self):
        """
        Move character up and down for jump animation.
        """
        frame = self._jump_frames[self.jump_index % len(self._jump_frames)]
        self._canvas.itemconfig(self._character_id, image=frame)
        self.jump_index += 1

        dy = self.jump_offset if self.going_up else -self.jump_offset
        self._canvas.move(self._character_id, 0, -dy)

        current_y = self._canvas.coords(self._character_id)[1]

        if self.going_up and current_y <= self._char_y - self.jump_height:
            self.going_up = False
        elif not self.going_up and current_y >= self._char_y:
            self._canvas.coords(self._character_id, self._char_x, self._char_y)
            self.jumps_remaining -= 1
            if self.jumps_remaining <= 0:
                return self.frame.after(800, self.cleanup)
            self.going_up = True

        self.frame.after(60, self._do_jump_frame)

    def cleanup(self):
        """
        Cleanup after the animation completes and transition to the next screen.
        """
        self._on_done()
