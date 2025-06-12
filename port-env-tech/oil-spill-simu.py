import numpy as np
import matplotlib.pyplot as plt

# --- Constants and Given Values ---
V0 = 200000  # m^3, Volume of spilled oil
R0 = 78      # m, Initial radius of the oil slick
Pa = 1024    # kg/m^3, Density of seawater (1.024 g/cm^3 converted to kg/m^3)
P = 850      # kg/m^3, Density of crude oil (0.85 g/cm^3 converted to kg/m^3)
g = 9.81     # m/s^2, Acceleration due to gravity

# --- Calculate 'v' term ---
# This 'v' is a calculated value based on the formula you provided,
# not a direct velocity in m/s.
v_term = (Pa - P) * V0 / Pa
print(f"Calculated 'v' term: {v_term:.2f}")

# --- Time array ---
# Let's consider time in hours and convert to seconds for calculations.
# We'll plot for a few days to see the spread.
time_hours = np.linspace(0, 72, 500) # From 0 to 72 hours (3 days)
time_seconds = time_hours * 3600     # Convert hours to seconds

# --- Calculate Radius (R) and Area (S) over time ---
R = np.sqrt(4 * time_seconds * np.sqrt(2 * g * v_term / np.pi) + R0**2)
S = R**2 * np.pi

# specific_times_minutes = [20.5, 50, 70.5]

# print("--- Radius (R) at specific times ---")
# for t_minutes in specific_times_minutes:
#     t_second = t_minutes * 60  # Convert minutes to seconds
#     R = np.sqrt(4 * t_second * np.sqrt(2 * g * v_term / np.pi) + R0**2)
#     print(f"Time (min): {t_minutes}, Radius (R): {R:.2f} m")

# --- Plotting ---
plt.figure(figsize=(12, 6))

# Plot for Radius (R)
plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
plt.plot(time_hours, R, label='Oil Spill Radius (R)')
plt.title('Oil Spill Radius over Time')
plt.xlabel('Time (hours)')
plt.ylabel('Radius (m)')
plt.grid(True)
plt.legend()

# Plot for Area (S)
plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
plt.plot(time_hours, S / (10**6), label='Oil Spill Area (S)', color='orange')
plt.title('Oil Spill Area over Time')
plt.xlabel('Time (hours)')
plt.ylabel('Area (km²)') # Display area in km^2 for better readability
plt.grid(True)
plt.legend()

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.savefig('oil-spill-simu.png')
plt.show()