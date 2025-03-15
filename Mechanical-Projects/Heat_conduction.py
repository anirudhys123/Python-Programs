import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation

def heat_conduction_1D(length=1.0, nx=20, alpha=0.01, dt=0.001, time_steps=200):
    dx = length / (nx - 1)
    r = alpha * dt / dx**2
    
    # Initial temperature profile
    T = np.ones(nx) * 20  # Initial temperature (20°C everywhere)
    T[0], T[-1] = 100, 50  # Boundary conditions (fixed temperatures)
    
    T_hist = [T.copy()]
    
    for _ in range(time_steps):
        T_new = T.copy()
        for i in range(1, nx - 1):
            T_new[i] = T[i] + r * (T[i+1] - 2*T[i] + T[i-1])
        T = T_new.copy()
        T_hist.append(T.copy())
    
    return np.array(T_hist)

def animate_heat():
    global length, nx, alpha, dt, time_steps
    
    length = float(length_entry.get())
    nx = int(nx_entry.get())
    alpha = float(alpha_entry.get())
    dt = float(dt_entry.get())
    time_steps = int(time_steps_entry.get())
    
    T_hist = heat_conduction_1D(length, nx, alpha, dt, time_steps)
    x = np.linspace(0, length, nx)
    
    fig, ax = plt.subplots()
    line, = ax.plot(x, T_hist[0], 'r-', linewidth=2)
    ax.set_ylim(0, 120)
    ax.set_xlabel("Rod Length")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("1D Heat Conduction in a Rod")
    
    def update(frame):
        line.set_ydata(T_hist[frame])
        return line,
    
    ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=50, blit=True)
    plt.show()

# Tkinter GUI
root = tk.Tk()
root.title("1D Heat Conduction Simulator")

tk.Label(root, text="Rod Length (m):").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "1.0")

tk.Label(root, text="Grid Points (nx):").pack()
nx_entry = tk.Entry(root)
nx_entry.pack()
nx_entry.insert(0, "20")

tk.Label(root, text="Thermal Diffusivity (alpha):").pack()
alpha_entry = tk.Entry(root)
alpha_entry.pack()
alpha_entry.insert(0, "0.01")

tk.Label(root, text="Time Step (dt):").pack()
dt_entry = tk.Entry(root)
dt_entry.pack()
dt_entry.insert(0, "0.001")

tk.Label(root, text="Time Steps:").pack()
time_steps_entry = tk.Entry(root)
time_steps_entry.pack()
time_steps_entry.insert(0, "200")

ttk.Button(root, text="Run Simulation", command=animate_heat).pack()
root.mainloop()