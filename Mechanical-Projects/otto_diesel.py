
"""
Problem Statement:
-------------------
This program simulates and visualizes the ideal Otto and Diesel cycles using thermodynamic principles.
The Otto cycle is modeled for a spark-ignition engine, assuming an adiabatic compression and expansion process.
The Diesel cycle is modeled for a compression-ignition engine, considering an additional constant pressure heat 
addition phase.

Key Features:
- Simulates pressure-volume (P-V) diagrams for both cycles.
- Computes theoretical efficiency for each cycle based on the compression ratio.
- Uses ideal gas assumptions for thermodynamic calculations.
- Provides graphical representation of the cycle with annotations.

Parameters:
- Compression Ratio (r): Ratio of initial to final volume during compression.
- Cutoff Ratio (rc) [Diesel Cycle]: Ratio of volume before and after heat addition.
- Gamma (γ): Specific heat ratio (Cp/Cv) of the working gas.
- Initial Conditions: Assumes atmospheric pressure (1 atm) and room temperature (300 K).

Expected Outcome:
- P-V diagrams for both Otto and Diesel cycles with clearly marked processes.
- Theoretical efficiency values for both cycles based on given parameters.

Usage:
Simply run the script to visualize and analyze the Otto and Diesel cycles.
"""

import numpy as np
import matplotlib.pyplot as plt

def otto_cycle(gamma=1.4, compression_ratio=8):
    """Simulates and plots the Otto cycle (ideal gas assumption)."""
    P1, T1 = 1, 300  # Initial pressure (atm) and temperature (K)
    V1 = 1  # Initial volume (arbitrary unit)
    V2 = V1 / compression_ratio  # Compressed volume
    
    # Process 1-2 (Compression - Adiabatic)
    T2 = T1 * (V1 / V2) ** (gamma - 1)
    P2 = P1 * (T2 / T1) * (V1 / V2)
    
    # Process 2-3 (Heat Addition - Constant Volume)
    T3 = 1800  # Assumed peak temperature (K)
    P3 = P2 * (T3 / T2)
    V3 = V2  # Constant volume heat addition
    
    # Process 3-4 (Expansion - Adiabatic)
    V4 = V1  # Returns to initial volume
    T4 = T3 * (V3 / V4) ** (gamma - 1)
    P4 = P3 * (T4 / T3) * (V3 / V4)
    
    # Efficiency Calculation (Ideal Otto Cycle)
    efficiency = 1 - (1 / compression_ratio ** (gamma - 1))
    
    # Plot P-V Diagram
    volumes = [V1, V2, V3, V4, V1]
    pressures = [P1, P2, P3, P4, P1]
    plt.figure(figsize=(8, 6))
    plt.plot(volumes, pressures, 'bo-', linewidth=3, marker='o', markersize=8, label='Otto Cycle')
    plt.fill_between(volumes, pressures, color='cyan', alpha=0.2)
    
    # Annotate points
    for i, (v, p) in enumerate(zip(volumes, pressures), 1):
        plt.annotate(f"{i}", (v, p), fontsize=14, fontweight='bold', color='black')
    
    plt.xlabel('Volume', fontsize=14)
    plt.ylabel('Pressure', fontsize=14)
    plt.title('Otto Cycle P-V Diagram', fontsize=16, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    print(f"Otto Cycle Efficiency: {efficiency * 100:.2f}%")

def diesel_cycle(gamma=1.4, compression_ratio=15, cutoff_ratio=2):
    """Simulates and plots the Diesel cycle (ideal gas assumption)."""
    P1, T1 = 1, 300  # Initial pressure (atm) and temperature (K)
    V1 = 1  # Initial volume
    V2 = V1 / compression_ratio  # Compressed volume
    
    # Process 1-2 (Compression - Adiabatic)
    T2 = T1 * (V1 / V2) ** (gamma - 1)
    P2 = P1 * (T2 / T1) * (V1 / V2)
    
    # Process 2-3 (Heat Addition - Constant Pressure)
    V3 = cutoff_ratio * V2
    T3 = T2 * (V3 / V2)
    P3 = P2  # Constant pressure
    
    # Process 3-4 (Expansion - Adiabatic)
    V4 = V1
    T4 = T3 * (V3 / V4) ** (gamma - 1)
    P4 = P3 * (T4 / T3) * (V3 / V4)
    
    # Efficiency Calculation (Ideal Diesel Cycle)
    efficiency = 1 - ((1 / compression_ratio ** (gamma - 1)) * ((T4 - T1) / (T3 - T2)))
    
    # Plot P-V Diagram
    volumes = [V1, V2, V3, V4, V1]
    pressures = [P1, P2, P3, P4, P1]
    plt.figure(figsize=(8, 6))
    plt.plot(volumes, pressures, 'ro-', linewidth=3, marker='o', markersize=8, label='Diesel Cycle')
    plt.fill_between(volumes, pressures, color='orange', alpha=0.2)
    
    # Annotate points
    for i, (v, p) in enumerate(zip(volumes, pressures), 1):
        plt.annotate(f"{i}", (v, p), fontsize=14, fontweight='bold', color='black')
    
    plt.xlabel('Volume', fontsize=14)
    plt.ylabel('Pressure', fontsize=14)
    plt.title('Diesel Cycle P-V Diagram', fontsize=16, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    print(f"Diesel Cycle Efficiency: {efficiency * 100:.2f}%")

# Run the simulations
otto_cycle()
diesel_cycle()
