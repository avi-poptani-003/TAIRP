import tkinter as tk
from tkinter import messagebox
import threading
import time

class CountdownApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("480x300")
        self.window.title("Countdown Timer")
        self.window.configure(bg="#1e1e2f")

        self.main_frame = tk.Frame(self.window, bg="#1e1e2f")
        self.main_frame.pack(expand=True)

        self.input_time = tk.Entry(self.main_frame, font=("Arial", 28), justify="center", fg="gray")
        self.input_time.insert(0, "HH:MM:SS")
        self.input_time.bind("<FocusIn>", self.clear_placeholder)
        self.input_time.bind("<FocusOut>", self.add_placeholder)
        self.input_time.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.start_btn = tk.Button(self.main_frame, text="Start", font=("Arial", 20), bg="#28a745", fg="white", command=self.start_timer_thread)
        self.start_btn.grid(row=1, column=0, pady=10, padx=10)

        self.reset_btn = tk.Button(self.main_frame, text="Reset", font=("Arial", 20), bg="#dc3545", fg="white", command=self.reset_timer)
        self.reset_btn.grid(row=1, column=1, pady=10, padx=10)

        self.time_display = tk.Label(self.main_frame, text="Time: 00:00:00", font=("Arial", 30), bg="#1e1e2f", fg="white")
        self.time_display.grid(row=2, column=0, columnspan=2, pady=20)

        self.timer_running = False

        self.window.mainloop()

    def clear_placeholder(self, event):
        if self.input_time.get() == "HH:MM:SS":
            self.input_time.delete(0, tk.END)
            self.input_time.config(fg="black")

    def add_placeholder(self, event):
        if not self.input_time.get():
            self.input_time.insert(0, "HH:MM:SS")
            self.input_time.config(fg="gray")

    def start_timer_thread(self):
        if not self.timer_running:
            self.timer_running = True
            threading.Thread(target=self.run_timer).start()

    def run_timer(self):
        try:
            h, m, s = self.parse_time(self.input_time.get())
            total_seconds = h * 3600 + m * 60 + s
        except ValueError:
            self.time_display.config(text="Invalid time format")
            return

        while total_seconds > 0 and self.timer_running:
            total_seconds -= 1
            h, remainder = divmod(total_seconds, 3600)
            m, s = divmod(remainder, 60)
            self.time_display.config(text=f"Time: {h:02}:{m:02}:{s:02}")
            self.window.update()
            time.sleep(1)

        if self.timer_running:
            messagebox.showinfo("Countdown Timer", "Time's up!")
            self.timer_running = False

    def parse_time(self, time_str):
        parts = time_str.split(":")
        if len(parts) == 3:
            return int(parts[0]), int(parts[1]), int(parts[2])
        elif len(parts) == 2:
            return 0, int(parts[0]), int(parts[1])
        elif len(parts) == 1:
            return 0, 0, int(parts[0])
        else:
            raise ValueError("Invalid time format")

    def reset_timer(self):
        self.timer_running = False
        self.time_display.config(text="Time: 00:00:00")

if __name__ == "__main__":
    CountdownApp()
