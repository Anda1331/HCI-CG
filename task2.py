import numpy as np

# Create a 300 x 400 x 3 image array
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Fill the four quadrants
# Top-left: Red
img[:150, :200] = [255, 0, 0]

# Top-right: Green
img[:150, 200:] = [0, 255, 0]

# Bottom-left: Blue
img[150:, :200] = [0, 0, 255]

# Bottom-right: White
img[150:, 200:] = [255, 255, 255]

# Display matrix information
print("\n--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) :", img.shape)
print("Data Type :", img.dtype)
print("Total Elements :", img.size, "values")
print("Memory Footprint :", img.nbytes, "bytes")