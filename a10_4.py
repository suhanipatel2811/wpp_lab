import numpy as np

# Step 1: Generate N random 2D points
N = 10  # You can change N to any value >= 10
cartesian_points = np.random.uniform(-10, 10, (N, 2))  # Random x, y in range [-10, 10]

# Step 2: Convert to polar coordinates
x = cartesian_points[:, 0]
y = cartesian_points[:, 1]

r = np.sqrt(x**2 + y**2)               # Radius
theta = np.arctan2(y, x)               # Angle in radians

# Combine into polar array (N x 2): [r, theta]
polar_points = np.column_stack((r, theta))

# Step 3: Display results
print("Cartesian Coordinates (x, y):\n", cartesian_points)
print("\nPolar Coordinates (r, θ in radians):\n", polar_points)
