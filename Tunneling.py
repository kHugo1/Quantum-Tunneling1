import numpy as np
import matplotlib.pyplot as plt


HBAR = 1.054571817E-34


MASS_E = 9.10938356e-31

eV_in_Joules = 1.602176634e-19

print("--- Quantum Tunnelling Simulator Setup ---")
print("We will simulate a 1D quantum tunnelling problem.")
print("This requires defining the particle and the potential barrier (the 'wall').")
print("\n--- Particle Parameters ---")

# Get Particle Mass (m)
print("First, the mass of the particle.")
print(f"For perspective, an electron weighs {MASS_E:.4e} kg")
m_input = float(input("Enter particle mass in kg (Enter 0 for default electron mass): "))
if m_input == 0:
    m = MASS_E
    print(f"Using electron mass: {m:.4e} kg")
else:
    m = m_input
    print(f"Using custom mass: {m:.4e} kg")

# Get Barrier Height (V_0)
print("\n--- Barrier Parameters ---")
print("Next, the barrier's height (V_0). This is the energy the particle needs to 'classically' pass. It can be seen as a measurement of how hard the wall is to penetrate")
V_0_eV = float(input("Enter barrier height in electron-volts (eV) (e.g., 1.0): "))
V_0 = V_0_eV * eV_in_Joules
print(f"Barrier height set to {V_0_eV} eV (which is {V_0:.4e} Joules)")

# Get Barrier Width (a)
print("\nFinally, the barrier's width (a). This is how thick the 'wall' is.")
a_nm = float(input("Enter barrier width in nanometers (nm) (e.g., 1.0): "))
a = a_nm * 1e-9
print(f"Barrier width set to {a_nm} nm (which is {a:.4e} meters)")



print("--- Start of Simulation ---")
print("The first step of the calculation is the calculating the tunneling probability for a range of different energy values for the particle")

num_points = int(input("Enter the number of different energy values(A higher number will lead to a smoother graph): "))
EValues = np.linspace(0, V_0 * 0.999, num_points)

# Compute Values and stuff
def gamma_compute(E, V_0, m):
    gamma = np.sqrt((2 * m * (V_0 - E)) / (HBAR**2))
    return gamma

def tunnel_prob(gamma, a):
    prob = np.exp(-2 * gamma * a)
    return prob

GammaV = gamma_compute(EValues, V_0, m)
TunnelProb = tunnel_prob(GammaV, a)



# Graphing
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(EValues / eV_in_Joules, TunnelProb) 


ax.set_title(f"Quantum Tunnelling (Barrier: {a_nm} nm wide, {V_0_eV} eV high)")
ax.set_xlabel(f"Particle Energy ($E$) in eV")

ax.set_ylabel("Tunnelling Probability ($T$) [1.0 = 100%]")


ax.set_yscale('log')

ax.set_ylim(1e-10, 1.1)
ax.set_xlim(0, V_0_eV)
ax.grid(True, which="both", linestyle='--')

plt.tight_layout()
plt.show()