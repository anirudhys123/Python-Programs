"""
Problem Statement:
------------------
This program simulates 1D transient heat conduction in a rod using 
the explicit Finite Difference Method (FDM). The heat equation is given by:

    ∂T/∂t = α * ∂²T/∂x²

where:
- T(x,t) is the temperature at position x and time t.
- α (thermal diffusivity) determines how fast heat spreads through the material.

Boundary Conditions:
--------------------
- Left boundary (x=0): Fixed temperature at 100°C.
- Right boundary (x=L): Fixed temperature at 50°C.
- Initial Condition: Temperature at 20°C everywhere except the boundaries.

Simulation Details:
-------------------
- The rod is 1 meter long.
- The simulation uses Nx = 50 spatial points.
- A time step (dt) of 0.001 seconds is used to maintain stability.
- The solution is computed over 500 time steps.
- Results are visualized as temperature distribution over the length of the rod at different time intervals.

The program implements an explicit finite difference approach:

    T_new[i] = T[i] + (α * dt / dx²) * (T[i+1] - 2*T[i] + T[i-1])

After running, the program generates a graph showing how the temperature 
evolves over time.

"""



import numpy as np
import matplotlib.pyplot as plt

# Define parameters
L = 1.0  # Length of the rod (m)
Nx = 50  # Number of spatial points
dx = L / (Nx - 1)  # Spatial step size
alpha = 0.01  # Thermal diffusivity (m^2/s)

T_left = 100  # Left boundary temperature (°C)
T_right = 50   # Right boundary temperature (°C)
T_initial = 20  # Initial temperature (°C)

dt = 0.001  # Time step (s)
Nt = 500  # Number of time steps

# Stability condition (explicit scheme): dt <= (dx^2) / (2*alpha)
assert dt <= (dx**2) / (2 * alpha), "Time step too large for stability!"

# Initialize temperature field
T = np.ones(Nx) * T_initial
T[0] = T_left
T[-1] = T_right

# Store temperature history for visualization
T_history = [T.copy()]

# Time-stepping loop (explicit finite difference method)
for _ in range(Nt):
    T_new = T.copy()
    for i in range(1, Nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i+1] - 2*T[i] + T[i-1])
    T = T_new.copy()
    T_history.append(T.copy())

# Convert T_history to numpy array for plotting
T_history = np.array(T_history)

# Plot temperature distribution over time
plt.figure(figsize=(10, 6))
for i in range(0, Nt, Nt//10):  # Plot at different time intervals
    plt.plot(np.linspace(0, L, Nx), T_history[i, :], label=f't={i*dt:.2f}s')

plt.xlabel('Position (m)')
plt.ylabel('Temperature (°C)')
plt.title('1D Heat Conduction Over Time')
plt.legend()
plt.grid(True)
plt.show()
