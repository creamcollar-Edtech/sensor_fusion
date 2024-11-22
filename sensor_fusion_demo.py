import numpy as np
import matplotlib.pyplot as plt

# Simulated data
np.random.seed(42)  # Ensure reproducibility
gps_x = np.random.uniform(0, 100, 50)  # GPS X coordinates
gps_y = np.random.uniform(0, 100, 50)  # GPS Y coordinates
radar_x = gps_x + np.random.normal(0, 2, 50)  # Slightly offset X for radar
radar_y = gps_y + np.random.normal(0, 2, 50)  # Slightly offset Y for radar

# Plot fused data
plt.figure(figsize=(8, 6))
plt.scatter(gps_x, gps_y, c="blue", label="GPS", alpha=0.7)
plt.scatter(radar_x, radar_y, c="red", label="Radar", alpha=0.7)
plt.title("Sensor Fusion: GPS and Radar Data")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.legend()
plt.grid()
plt.savefig("examples/sample_output.png")  # Save the output image
plt.show()
