import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox

def calculate_cfd():
    try:
        # Get inputs from GUI
        L = float(entry_L.get())  # Length of HE (m)
        D_inner = float(entry_D_inner.get())  # Inner pipe diameter (m)
        D_outer = float(entry_D_outer.get())  # Outer pipe diameter (m)
        T_hot_in = float(entry_T_hot_in.get())  # Hot fluid inlet temp (°C)
        T_cold_in = float(entry_T_cold_in.get())  # Cold fluid inlet temp (°C)
        m_hot = float(entry_m_hot.get())  # Mass flow rate of hot fluid (kg/s)
        m_cold = float(entry_m_cold.get())  # Mass flow rate of cold fluid (kg/s)
        cp_hot = float(entry_cp_hot.get())  # Specific heat of hot fluid (J/kg.K)
        cp_cold = float(entry_cp_cold.get())  # Specific heat of cold fluid (J/kg.K)
        k_pipe = float(entry_k_pipe.get())  # Pipe thermal conductivity (W/m.K)
        U = float(entry_U.get())  # User-input heat transfer coefficient

        # Increase resolution for accuracy
        N = 500  # More divisions for better accuracy
        dx = L / N

        # Initialize temperature arrays
        T_hot = np.zeros(N+1)
        T_cold = np.zeros(N+1)
        T_hot[0] = T_hot_in
        T_cold[0] = T_cold_in

        # Iterative energy balance
        for i in range(N):
            dQ = U * np.pi * D_inner * dx * (T_hot[i] - T_cold[i])
            dT_hot = dQ / (m_hot * cp_hot)
            dT_cold = dQ / (m_cold * cp_cold)

            T_hot[i+1] = T_hot[i] - dT_hot
            T_cold[i+1] = T_cold[i] + dT_cold

        # Extract final outlet temperatures
        T_hot_out = T_hot[-1]
        T_cold_out = T_cold[-1]

        # Effectiveness Calculation (NTU Method)
        C_min = min(m_hot * cp_hot, m_cold * cp_cold)
        Q_max = C_min * (T_hot_in - T_cold_in)
        Q_actual = m_cold * cp_cold * (T_cold_out - T_cold_in)
        effectiveness = Q_actual / Q_max

        # Display results
        messagebox.showinfo("Results", 
            f"Hot Fluid Outlet Temp: {T_hot_out:.2f}°C\n"
            f"Cold Fluid Outlet Temp: {T_cold_out:.2f}°C\n"
            f"Heat Exchanger Effectiveness: {effectiveness:.4f}")

        # Plot temperature distribution
        sns.set_theme(style="darkgrid")
        x = np.linspace(0, L, N+1)
        plt.figure(figsize=(10, 6))
        plt.plot(x, T_hot, label="Hot Fluid Temperature", color='r', linewidth=2.5)
        plt.plot(x, T_cold, label="Cold Fluid Temperature", color='b', linewidth=2.5, linestyle='--')

        plt.xlabel("Length of Heat Exchanger (m)", fontsize=14)
        plt.ylabel("Temperature (°C)", fontsize=14)
        plt.title("Optimized Temperature Distribution", fontsize=16, fontweight='bold')
        plt.legend(fontsize=12)
        plt.grid(True, linestyle="--", linewidth=0.5)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Optimized CFD Analysis - Counterflow HE")
root.geometry("450x600")

# Labels and Entry Fields
tk.Label(root, text="Length of HE (m):").pack()
entry_L = tk.Entry(root)
entry_L.pack()

tk.Label(root, text="Inner Pipe Diameter (m):").pack()
entry_D_inner = tk.Entry(root)
entry_D_inner.pack()

tk.Label(root, text="Outer Pipe Diameter (m):").pack()
entry_D_outer = tk.Entry(root)
entry_D_outer.pack()

tk.Label(root, text="Hot Fluid Inlet Temp (°C):").pack()
entry_T_hot_in = tk.Entry(root)
entry_T_hot_in.pack()

tk.Label(root, text="Cold Fluid Inlet Temp (°C):").pack()
entry_T_cold_in = tk.Entry(root)
entry_T_cold_in.pack()

tk.Label(root, text="Hot Fluid Mass Flow Rate (kg/s):").pack()
entry_m_hot = tk.Entry(root)
entry_m_hot.pack()

tk.Label(root, text="Cold Fluid Mass Flow Rate (kg/s):").pack()
entry_m_cold = tk.Entry(root)
entry_m_cold.pack()

tk.Label(root, text="Specific Heat of Hot Fluid (J/kg.K):").pack()
entry_cp_hot = tk.Entry(root)
entry_cp_hot.pack()

tk.Label(root, text="Specific Heat of Cold Fluid (J/kg.K):").pack()
entry_cp_cold = tk.Entry(root)
entry_cp_cold.pack()

tk.Label(root, text="Pipe Thermal Conductivity (W/m.K):").pack()
entry_k_pipe = tk.Entry(root)
entry_k_pipe.pack()

tk.Label(root, text="Overall Heat Transfer Coefficient (U) (W/m².K):").pack()
entry_U = tk.Entry(root)
entry_U.pack()

# Button to Calculate
tk.Button(root, text="Calculate", command=calculate_cfd).pack()

# Run GUI Loop
root.mainloop()
