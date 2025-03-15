import numpy as np
import matplotlib.pyplot as plt

# Beam properties
E = 200e9  # Young's modulus (Pa)
I = 8.333e-6  # Moment of inertia (m^4)
L = 1.0  # Length of beam (m)
P = 1000  # Load at free end (N)
num_elements = 20  # Increased number of elements for better resolution
num_nodes = num_elements + 1

# Element length
le = L / num_elements

# Global stiffness matrix (2 DOF per node)
K = np.zeros((2 * num_nodes, 2 * num_nodes))

# Assemble the global stiffness matrix
for i in range(num_elements):
    k_local = (E * I / le**3) * np.array([
        [12, 6*le, -12, 6*le],
        [6*le, 4*le**2, -6*le, 2*le**2],
        [-12, -6*le, 12, -6*le],
        [6*le, 2*le**2, -6*le, 4*le**2]
    ])

    node1 = i * 2
    node2 = node1 + 2
    K[node1:node2+2, node1:node2+2] += k_local  # Correct indexing

# Apply boundary conditions (cantilever: fix displacement and rotation at node 0)
K_reduced = K[2:, 2:]  # Removing first two rows and columns (fixed DOFs)

# Load vector
F = np.zeros(2 * num_nodes)
F[-2] = P  # Apply load at last node in vertical direction

# Solve for deflection
F_reduced = F[2:]  # Adjusting for removed DOFs
displacements = np.linalg.solve(K_reduced, F_reduced)
displacements = np.insert(displacements, 0, [0, 0])  # Fixed end (zero displacement & rotation)

# Extract vertical deflection only
y_displacements = displacements[::2]  # Only take y-direction displacements

# Plot results
x = np.linspace(0, L, num_nodes)
plt.figure(figsize=(10, 6))
plt.plot(x, y_displacements * 1e3, marker="o", linestyle="-", color="b", label="FEA Deflection")

# Analytical solution (for validation)
x_analytical = np.linspace(0, L, 100)
y_analytical = (-P * x_analytical**3) / (6 * E * I) * (3 * L - x_analytical)
plt.plot(x_analytical, y_analytical * 1e3, linestyle="--", color="r", label="Analytical Solution")

# Enhancing the graph
plt.xlabel("Beam Length (m)", fontsize=12, fontweight="bold")
plt.ylabel("Deflection (mm)", fontsize=12, fontweight="bold")
plt.title("FEA-Based Beam Deflection (Cantilever Beam) vs Analytical Solution", fontsize=14, fontweight="bold")
plt.legend(fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
