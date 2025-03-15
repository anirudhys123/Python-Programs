import tkinter as tk
from tkinter import messagebox
import time

# Initialize the Tkinter window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("250x150")

# Global variables for the stopwatch
start_time = 0
elapsed_time = 0
running = False

def start():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_time
        running = True
        update_timer()

def stop():
    global running
    if running:
        root.after_cancel(update_timer_job)  # Stop the timer updates
        running = False

def reset():
    global start_time, elapsed_time, running
    start_time = 0
    elapsed_time = 0
    running = False
    timer_label.config(text="00:00:00")

def update_timer():
    global elapsed_time, update_timer_job
    if running:
        elapsed_time = time.time() - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        timer_label.config(text=formatted_time)
        update_timer_job = root.after(1000, update_timer)  # Update every second

# Timer display label
timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 30))
timer_label.pack(pady=20)

# Start, Stop, and Reset buttons
start_button = tk.Button(root, text="Start", command=start)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(side="left", padx=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side="left", padx=10)

# Start the Tkinter event loop
root.mainloop()
