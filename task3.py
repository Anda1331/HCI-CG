import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
image = Image.open("image.jpeg").convert("RGB")
img = np.array(image)

# Extract individual color channels
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

# Create isolated color images
red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

red_only[:, :, 0] = red
green_only[:, :, 1] = green
blue_only[:, :, 2] = blue

# Print channel extraction summary
print("\n--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape :", img.shape)
print(f"Red Channel 2D Shape : {red.shape} | Mean Intensity: {red.mean():.2f}")
print(f"Green Channel 2D Shape: {green.shape} | Mean Intensity: {green.mean():.2f}")
print(f"Blue Channel 2D Shape : {blue.shape} | Mean Intensity: {blue.mean():.2f}")

# Create 2 x 3 subplot layout
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Top row: Red-only, Green-only, Blue-only
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only")

# Bottom row: Grayscale channel intensity maps
axes[1, 0].imshow(red, cmap="gray")
axes[1, 0].set_title("Red Channel - Grayscale")

axes[1, 1].imshow(green, cmap="gray")
axes[1, 1].set_title("Green Channel - Grayscale")

axes[1, 2].imshow(blue, cmap="gray")
axes[1, 2].set_title("Blue Channel - Grayscale")

# Remove axes
for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()
plt.show()

print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")