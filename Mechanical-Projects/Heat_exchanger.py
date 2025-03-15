import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Heat Exchanger Effectiveness Calculation
def effectiveness(Cr, NTU, type):
    if type == 'Parallel':
        return (1 - np.exp(-NTU * (1 + Cr))) / (1 + Cr)
    elif type == 'Counterflow':
        return (1 - np.exp(-NTU * (1 - Cr))) / (1 - Cr * np.exp(-NTU * (1 - Cr)))
    elif type == 'Crossflow':
        return 1 - np.exp(-NTU * (1 + Cr))
    else:
        return None

# Plot Temperature Distribution for all types
def plot_temperature(T_hot_in, T_cold_in, C_hot, C_cold):
    global result_label  # Make sure result_label is accessible
    
    NTU = np.linspace(0, 10, 100)
    Cr = C_cold / C_hot if C_hot >= C_cold else C_hot / C_cold
    
    types = ['Parallel', 'Counterflow', 'Crossflow']
    plt.figure(figsize=(8, 6))
    
    final_temperatures = {}
    
    for type in types:
        effectiveness_values = [effectiveness(Cr, ntu, type) for ntu in NTU]
        T_hot_out = T_hot_in - np.array(effectiveness_values) * (T_hot_in - T_cold_in)
        T_cold_out = T_cold_in + np.array(effectiveness_values) * (T_hot_in - T_cold_in) * (C_hot / C_cold)
        plt.plot(NTU, T_hot_out, label=f'Hot Stream {type}')
        plt.plot(NTU, T_cold_out, label=f'Cold Stream {type}', linestyle='dashed')
        
        final_temperatures[type] = (T_hot_out[-1], T_cold_out[-1])
    
    plt.xlabel('NTU')
    plt.ylabel('Temperature (°C)')
    plt.title('Heat Exchanger Performance Comparison')
    plt.grid()
    
    # Move legend outside the plot
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    
    plt.show()
    
    # Display final results
    result_text = "Final Outlet Temperatures:\n"
    for type, temps in final_temperatures.items():
        result_text += f"{type} - Hot: {temps[0]:.2f}°C, Cold: {temps[1]:.2f}°C\n"
    
    result_label.config(text=result_text)

# GUI Application
def calculate():
    T_hot_in = float(entry_hot_in.get())
    T_cold_in = float(entry_cold_in.get())
    C_hot = float(entry_C_hot.get())
    C_cold = float(entry_C_cold.get())
    
    plot_temperature(T_hot_in, T_cold_in, C_hot, C_cold)

# Tkinter GUI
top = tk.Tk()
top.title("Heat Exchanger Performance Analyzer")

tk.Label(top, text="Hot Stream Inlet Temperature (°C)").grid(row=0, column=0)
entry_hot_in = tk.Entry(top)
entry_hot_in.grid(row=0, column=1)


tk.Label(top, text="Cold Stream Inlet Temperature (°C)").grid(row=1, column=0)
entry_cold_in = tk.Entry(top)
entry_cold_in.grid(row=1, column=1)


tk.Label(top, text="Hot Stream Heat Capacity (W/K)").grid(row=2, column=0)
entry_C_hot = tk.Entry(top)
entry_C_hot.grid(row=2, column=1)


tk.Label(top, text="Cold Stream Heat Capacity (W/K)").grid(row=3, column=0)
entry_C_cold = tk.Entry(top)
entry_C_cold.grid(row=3, column=1)


tk.Button(top, text="Analyze", command=calculate).grid(row=4, column=1)

# Result display label
global result_label
result_label = tk.Label(top, text="", justify="left")
result_label.grid(row=5, column=0, columnspan=2)

top.mainloop()
