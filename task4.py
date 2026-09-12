import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
image = Image.open("image.jpeg").convert("RGB")
img = np.array(image)

# Downsampling factor
N = 8

# Downsample image using NumPy striding
downsampled = img[::N, ::N, :]

# Re-expand the downsampled image
reexpanded = np.repeat(
    np.repeat(downsampled, N, axis=0),
    N,
    axis=1
)

# Crop to original dimensions
reexpanded = reexpanded[:img.shape[0], :img.shape[1], :]

# Calculate reductions
height_reduction = (1 - downsampled.shape[0] / img.shape[0]) * 100
width_reduction = (1 - downsampled.shape[1] / img.shape[1]) * 100
memory_reduction = (1 - downsampled.nbytes / img.nbytes) * 100

# Print analysis
print("\n--- DOWNSAMPLING ANALYSIS (N = 8) ---")
print(f"Original Shape : {img.shape} | Memory: {img.nbytes:,} bytes")
print(f"Downsampled Shape : {downsampled.shape} | Memory: {downsampled.nbytes:,} bytes")
print(f"Re-expanded Shape : {reexpanded.shape} | Visual: Blocky Pixelation")
print(f"Height Reduction : {height_reduction:.2f}%")
print(f"Width Reduction : {width_reduction:.2f}%")
print(f"Memory Savings : {memory_reduction:.2f}%")

# Display original and pixelated images
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(reexpanded)
axes[1].set_title("Pixelated Image (N = 8)")
axes[1].axis("off")

plt.tight_layout()
plt.show()