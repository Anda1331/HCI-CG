# Task 2
# Step 1: Inputs and output
# Inputs: image width, image height, and bits per pixel (bpp).
# Output: uncompressed image memory in bytes.
#
# Step 2: Rule
# bytes = width * height * bpp / 8
#
# Step 3: Small example
# For 1920 x 1080 at 24 bpp:
# 1920 * 1080 * 24 / 8 = 6,220,800 bytes.
#
# Step 4: Python

def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    return width * height * bpp // 8


expected_bytes = 1920 * 1080 * 24 // 8

assert display_memory_bytes(1920, 1080, 24) == expected_bytes

print("Memory:", display_memory_bytes(1920, 1080, 24), "bytes")
print("Task 2 passed.")
