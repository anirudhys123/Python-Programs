import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_sfd_bmd():
    try:
        L = float(length_entry.get())
        P = float(load_entry.get())
        a = float(position_entry.get())
        
        # Calculate reactions at supports (Simply Supported Beam)
        Rb = (P * a) / L
        Ra = P - Rb
        
        # Shear Force Calculation
        x = np.linspace(0, L, 100)
        V = np.piecewise(x, [x < a, x >= a], [Ra, Ra - P])
        
        # Bending Moment Calculation
        M = np.piecewise(x, [x < a, x >= a], [lambda x: Ra * x, lambda x: Ra * x - P * (x - a)])
        
        # Clear previous plots
        ax1.clear()
        ax2.clear()
        
        # Plot SFD
        ax1.plot(x, V, label="Shear Force", color='royalblue', linewidth=2)
        ax1.fill_between(x, 0, V, color='lightblue', alpha=0.5)
        ax1.axhline(0, color='black', linewidth=1)
        ax1.set_title("Shear Force Diagram (SFD)", fontsize=16, fontweight='bold', color='navy')
        ax1.set_xlabel("Beam Length (m)", fontsize=14)
        ax1.set_ylabel("Shear Force (N)", fontsize=14)
        ax1.legend()
        ax1.grid(True, linestyle="--", alpha=0.7)
        
        # Plot BMD
        ax2.plot(x, M, label="Bending Moment", color='darkred', linewidth=2)
        ax2.fill_between(x, 0, M, color='lightcoral', alpha=0.5)
        ax2.axhline(0, color='black', linewidth=1)
        ax2.set_title("Bending Moment Diagram (BMD)", fontsize=16, fontweight='bold', color='maroon')
        ax2.set_xlabel("Beam Length (m)", fontsize=14)
        ax2.set_ylabel("Bending Moment (Nm)", fontsize=14)
        ax2.legend()
        ax2.grid(True, linestyle="--", alpha=0.7)
        
        # Update plots
        canvas.draw()
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid numbers.", font=("Arial", 14, "bold"), foreground="red")

# GUI Setup
root = tk.Tk()
root.title("SFD & BMD Calculator for Simply Supported Beam")
root.geometry("900x600")
root.configure(bg="#f0f8ff")  # Light azure background

# Heading Label
title_label = ttk.Label(root, text="SFD and BMD Calculator for Simply Supported Beam for a Single Point Load", 
                        font=("Arial", 16, "bold"), background="#f0f8ff", foreground="darkblue")
title_label.grid(row=0, column=0, padx=10, pady=10)

frame = ttk.Frame(root, padding=10, relief="solid", borderwidth=2)
frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
frame.configure(style="Custom.TFrame")

# Define Styles
style = ttk.Style()
style.configure("Custom.TFrame", background="#f0f8ff")

# Enhanced Button Styling
style.configure("Custom.TButton",
                font=("Arial", 14, "bold"),  # Increased font size
                padding=12,  # Increased padding for better appearance
                background="#007ACC",  # Bright blue background
                foreground="Black",  # White text
                borderwidth=3,  # Added border for prominence
                relief="raised")  # Raised effect for 3D look

style.map("Custom.TButton", 
          background=[("active", "#005a99")],  # Darker shade on hover
          relief=[("pressed", "sunken")])  # Pressed effect for better interaction

label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)

ttk.Label(frame, text="Beam Length (m):", font=label_font, background="#f0f8ff").grid(row=0, column=0, padx=5, pady=5, sticky='w')
length_entry = ttk.Entry(frame, font=entry_font, width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Point Load (N):", font=label_font, background="#f0f8ff").grid(row=1, column=0, padx=5, pady=5, sticky='w')
load_entry = ttk.Entry(frame, font=entry_font, width=10)
load_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Load Position (m):", font=label_font, background="#f0f8ff").grid(row=2, column=0, padx=5, pady=5, sticky='w')
position_entry = ttk.Entry(frame, font=entry_font, width=10)
position_entry.grid(row=2, column=1, padx=5, pady=5)

# Improved Calculate Button
calculate_button = ttk.Button(frame, text="🚀 Calculate SFD & BMD 🚀", command=calculate_sfd_bmd, style='Custom.TButton')
calculate_button.grid(row=3, column=0, columnspan=2, pady=15)

result_label = ttk.Label(frame, text="", font=label_font, background="#f0f8ff")
result_label.grid(row=4, column=0, columnspan=2)

# Matplotlib Figure - Maximized for Clear Display
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), facecolor="#ffffff")
fig.subplots_adjust(left=0.05, right=0.75, top=0.92, bottom=0.5, wspace=0.3)  # Adjusted margins for clarity
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

root.mainloop()