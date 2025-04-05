import tkinter as tk
from PIL import ImageTk, Image
import os, time


class SplashScreen(tk.Toplevel):
    def __init__(self, root, on_complete_callback):
        super().__init__(root)
        self.root = root
        self.on_complete = on_complete_callback

        self.overrideredirect(True)
        self.configure(bg="black")
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", "black")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Sprite data
        self.char_width = 256
        self.char_height = 256
        self.char_x = - self.char_width
        self.char_y = screen_height - 380
        self.character_id = None
        self.current_frame_index = 0

        # Logo data
        self.logo_img_raw = Image.open("assets/splash/sprite_logo.png").convert("RGBA").resize((400, 120))
        self.logo_img_tk = None
        self.logo_id = None
        self.logo_x = screen_width // 2
        self.logo_y = self.char_y - 60
        self.logo_opacity = 0

        # Load animations
        self.run_frames = self._load_frames("assets/splash/running")
        self.jump_frames = self._load_frames("assets/splash/jump_loop")

        # Timing
        self.start_time = time.perf_counter()

        self.after(10, self._start_animation)

    def _load_frames(self, folder):
        frames = []
        files = sorted(
            [f for f in os.listdir(folder) if f.endswith(".png")],
            key=lambda name: int(name.replace(".png", ""))
        )
        for file in files:
            path = os.path.join(folder, file)
            img = Image.open(path).resize((self.char_width, self.char_height))
            frames.append(ImageTk.PhotoImage(img))
        return frames

    def _start_animation(self):
        self.character_id = self.canvas.create_image(
            self.char_x, self.char_y, image=self.run_frames[0], anchor="nw"
        )
        self.logo_id = self.canvas.create_image(
            self.logo_x, self.logo_y, image="", anchor="center"
        )
        self._animate_loop()

    def _animate_loop(self):
        elapsed = (time.perf_counter() - self.start_time) * 1000  # milliseconds

        # --- Fade logo (0-1000ms)
        if elapsed <= 1000:
            alpha = int(255 * (elapsed / 1000))
            faded = self.logo_img_raw.copy()
            faded.putalpha(alpha)
            self.logo_img_tk = ImageTk.PhotoImage(faded)
            self.canvas.itemconfig(self.logo_id, image=self.logo_img_tk)

        # --- Run character (0–2000ms)
        if elapsed <= 2000:
            center_target = self.winfo_screenwidth() // 2 - (self.char_width // 2) + 40
            percent = min(elapsed / 2000, 1)
            new_x = int(-self.char_width + (center_target + self.char_width) * percent)
            self.char_x = new_x  # 🛠 Oppdater nåværende posisjon!

            self.canvas.coords(self.character_id, new_x, self.char_y)
            self._next_run_frame()

        # --- End run, begin jump
        if elapsed >= 2000 and not hasattr(self, "_jump_started"):
            self._jump_started = True
            self.after(100, self._jump_finish)

        # Continue animation loop
        if elapsed < 3200:
            self.after(33, self._animate_loop)  # ~30 FPS

    def _next_run_frame(self):
        self.current_frame_index = (self.current_frame_index + 1) % len(self.run_frames)
        self.canvas.itemconfig(self.character_id, image=self.run_frames[self.current_frame_index])

    def _jump_finish(self):
        self.jump_index = 0
        self.jumps_remaining = 4
        self.jump_height = 60
        self.going_up = True
        self.jump_direction = -1
        self.jump_offset = 10

        self._do_jump_frame()

    def _do_jump_frame(self):
        # Sett riktig spritebilde
        frame = self.jump_frames[self.jump_index % len(self.jump_frames)]
        self.canvas.itemconfig(self.character_id, image=frame)
        self.jump_index += 1

        # Flytt karakter opp eller ned
        dy = self.jump_offset if self.going_up else -self.jump_offset
        self.canvas.move(self.character_id, 0, -dy)

        current_y = self.canvas.coords(self.character_id)[1]

        if self.going_up and current_y <= self.char_y - self.jump_height:
            self.going_up = False
        elif not self.going_up and current_y >= self.char_y:
            self.canvas.coords(self.character_id, self.char_x, self.char_y)
            self.jumps_remaining -= 1
            if self.jumps_remaining <= 0:
                return self.after(800, self.cleanup)
            self.going_up = True

        self.after(60, self._do_jump_frame)

    def cleanup(self):
        self.destroy()
        self.on_complete(self.root)
