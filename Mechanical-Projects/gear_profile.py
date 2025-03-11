import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk

# Function to generate gear teeth
def generate_gear(radius, teeth, resolution=100):
    angles = np.linspace(0, 2 * np.pi, teeth * resolution)
    r = radius + 0.2 * radius * np.sin(teeth * angles / 2)  # Simulating teeth
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    return x, y

# Initialize gear parameters
teeth_1, teeth_2 = 10, 20  # Default teeth count
radius_1, radius_2 = 2, 4  # Default radii
speed = 0.1  # Default rotation speed

# Generate initial gear profiles
x1, y1 = generate_gear(radius_1, teeth_1)
x2, y2 = generate_gear(radius_2, teeth_2)

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

gear1, = ax.plot(x1, y1, 'b')
gear2, = ax.plot(x2 + radius_1 + radius_2, y2, 'r')

# Animation function
def update(frame):
    angle1 = frame * speed
    angle2 = -frame * speed * (teeth_1 / teeth_2)  # Reverse rotation for meshing
    
    x1_rot = x1 * np.cos(angle1) - y1 * np.sin(angle1)
    y1_rot = x1 * np.sin(angle1) + y1 * np.cos(angle1)
    
    x2_rot = x2 * np.cos(angle2) - y2 * np.sin(angle2)
    y2_rot = x2 * np.sin(angle2) + y2 * np.cos(angle2)
    
    gear1.set_data(x1_rot, y1_rot)
    gear2.set_data(x2_rot + radius_1 + radius_2, y2_rot)
    return gear1, gear2

ani = animation.FuncAnimation(fig, update, frames=360, interval=50, blit=True)

# Tkinter GUI for user input
root = tk.Tk()
root.title("Gear Motion Simulator")

tk.Label(root, text="Teeth on Gear 1").pack()
teeth1_entry = tk.Entry(root)
teeth1_entry.pack()
teeth1_entry.insert(0, str(teeth_1))

tk.Label(root, text="Teeth on Gear 2").pack()
teeth2_entry = tk.Entry(root)
teeth2_entry.pack()
teeth2_entry.insert(0, str(teeth_2))

tk.Label(root, text="Speed").pack()
speed_entry = tk.Entry(root)
speed_entry.pack()
speed_entry.insert(0, str(speed))

def update_values():
    global teeth_1, teeth_2, speed, x1, y1, x2, y2
    teeth_1 = int(teeth1_entry.get())
    teeth_2 = int(teeth2_entry.get())
    speed = float(speed_entry.get())
    
    # Recalculate gear profiles
    x1, y1 = generate_gear(radius_1, teeth_1)
    x2, y2 = generate_gear(radius_2, teeth_2)

    ani.event_source.stop()  # Stop previous animation
    ani.event_source.start()  # Restart animation

ttk.Button(root, text="Update", command=update_values).pack()

# Show Matplotlib plot without blocking Tkinter
plt.show(block=False)

root.mainloop()
