# Week 02 Lab: Image Processing Through a Four-Step Pipeline
# Course: Perceptual Computing / Computer Graphics and Human-Computer Interaction
#
# Student information intentionally omitted.
# The student should add Name, Roll number, and GitHub username before submission.
#
# Four-step structure used for each problem:
# 1. Inputs and output
# 2. Rule
# 3. Small example
# 4. Python implementation and test
#
# All image values are kept in the range 0-255 where applicable.

import numpy as np


# ---------------------------------------------------------------------------
# Worked Sample 1: RGB to Grayscale
# ---------------------------------------------------------------------------
# Step 1: Inputs and output
# Inputs: r, g, b in [0, 255]. Output: one grayscale integer in [0, 255].
#
# Step 2: Rule
# Y = 0.299R + 0.587G + 0.114B
#
# Step 3: Small example
# For (180, 120, 60):
# Y = 0.299(180) + 0.587(120) + 0.114(60) = 131.1 -> 131.
#
# Step 4: Python

def rgb_to_grayscale(r: int, g: int, b: int) -> int:
    """Convert one RGB pixel to a rounded grayscale luminosity value."""
    luminosity = 0.299 * r + 0.587 * g + 0.114 * b
    return int(round(luminosity))


sample_result = rgb_to_grayscale(180, 120, 60)
print("Sample 1 result:", sample_result)
assert sample_result == 131
assert rgb_to_grayscale(80, 80, 80) == 80
print("Sample 1 passed.")


# ---------------------------------------------------------------------------
# Worked Sample 2: Brightness and Contrast Adjustment
# ---------------------------------------------------------------------------
# Step 1: Inputs and output
# Input: a 2D grayscale NumPy array, alpha > 0, and numeric beta.
# Output: same shape, uint8, with values in [0, 255].
#
# Step 2: Rule
# O(x,y) = alpha * I(x,y) + beta
# Then clip to [0, 255].
#
# Step 3: Small example
# I = [[100, 150], [200, 50]], alpha = 1.5, beta = -20
# Result = [[130, 205], [255, 55]] after clipping.
#
# Step 4: Python

def adjust_brightness_contrast(
    image: np.ndarray, alpha: float, beta: float
) -> np.ndarray:
    """Apply O = alpha * I + beta and clip the result to [0, 255]."""
    image_float = image.astype(np.float32)
    adjusted = alpha * image_float + beta
    return np.clip(adjusted, 0, 255).astype(np.uint8)


sample_image = np.array([[100, 150], [200, 50]], dtype=np.uint8)
sample_output = adjust_brightness_contrast(sample_image, alpha=1.5, beta=-20)
expected_output = np.array([[130, 205], [255, 55]], dtype=np.uint8)
np.testing.assert_array_equal(sample_output, expected_output)
print(sample_output)

extra = adjust_brightness_contrast(
    np.array([[240]], dtype=np.uint8), alpha=1.0, beta=30
)
assert extra[0, 0] == 255
print("Sample 2 passed.")


# ===========================================================================
# Problem 1: Thresholding (1 mark)
# ===========================================================================
# Step 1: Inputs and output
# Input: a grayscale image and a threshold. Output: an image containing
# only black (0) and white (255).
#
# Step 2: Rule
# If pixel >= threshold, output 255; otherwise output 0.
#
# Step 3: Small example
# Input:
# 20  128  200
# 100 150  250
# With threshold 128:
# 0 255 255
# 0 255 255
#
# Step 4: Python

def threshold_image(image: np.ndarray, threshold: int) -> np.ndarray:
    """Convert a grayscale image to black and white."""
    return np.where(image >= threshold, 255, 0).astype(np.uint8)


problem_1_input = np.array(
    [[20, 128, 200], [100, 150, 250]], dtype=np.uint8
)
problem_1_expected = np.array(
    [[0, 255, 255], [0, 255, 255]], dtype=np.uint8
)
np.testing.assert_array_equal(
    threshold_image(problem_1_input, 128), problem_1_expected
)
print("Problem 1 passed")


# ===========================================================================
# Problem 2: Image Memory (1 mark)
# ===========================================================================
# Step 1: Inputs and output
# Inputs: width, height, and bits per pixel (bpp).
# Output: memory required in bytes.
#
# Step 2: Rule
# bytes = width * height * bpp / 8
#
# Step 3: Small example
# 1920 x 1080 at 24 bpp:
# 1920 * 1080 * 24 / 8 = 6,220,800 bytes.
#
# Step 4: Python

def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    """Return uncompressed image memory in bytes."""
    return width * height * bpp // 8


expected_bytes = 1920 * 1080 * 24 // 8
assert display_memory_bytes(1920, 1080, 24) == expected_bytes
print("Problem 2 passed")


# ===========================================================================
# Problem 3: Average 9 Pixels (1 mark)
# ===========================================================================
# Step 1: Inputs and output
# Input: nine pixel values in a 3 x 3 array.
# Output: one rounded average.
#
# Step 2: Rule
# average = sum of all 9 values / 9
#
# Step 3: Small example
# 10 20 10
# 30 50 30
# 10 20 10
# Sum = 190; 190 / 9 = 21.11..., which rounds to 21.
#
# Step 4: Python

def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    """Return the rounded average of 9 pixels."""
    return int(round(float(np.sum(neighborhood)) / 9))


problem_3_input = np.array(
    [[10, 20, 10], [30, 50, 30], [10, 20, 10]], dtype=np.uint8
)
assert mean_filter_3x3(problem_3_input) == 21
print("Problem 3 passed")


# ===========================================================================
# Problem 4: Change Image Contrast (1 mark)
# ===========================================================================
# Step 1: Inputs and output
# Input: an array plus old and new ranges.
# Output: the values mapped into the new range.
#
# Step 2: Rule
# new = (value - old_min) / (old_max - old_min)
#       * (new_max - new_min) + new_min
#
# Step 3: Small example
# Map [50, 100, 150] from [50, 150] to [0, 255]:
# 50 -> 0, 100 -> 127.5, 150 -> 255.
#
# Step 4: Python

def contrast_stretch(
    image: np.ndarray,
    in_min: float,
    in_max: float,
    out_min: float = 0.0,
    out_max: float = 255.0,
) -> np.ndarray:
    """Change image values from one range to another."""
    if in_max == in_min:
        raise ValueError("in_max and in_min must be different.")

    image_float = image.astype(np.float32)
    stretched = (image_float - in_min) / (in_max - in_min)
    stretched = stretched * (out_max - out_min) + out_min
    return np.clip(stretched, out_min, out_max)


problem_4_input = np.array([50, 100, 150], dtype=np.float32)
expected = np.array([0.0, 127.5, 255.0], dtype=np.float32)
np.testing.assert_allclose(
    contrast_stretch(problem_4_input, 50, 150), expected
)
print("Problem 4 passed")


# ===========================================================================
# Problem 5: Find an Edge with Sobel (1 mark)
# ===========================================================================
# Step 1: Inputs and output
# Input: a 3 x 3 grayscale block.
# Output: gx, gy, and edge strength.
#
# Step 2: Rule
# Gx = [-1 0 1; -2 0 2; -1 0 1]
# Gy = [-1 -2 -1; 0 0 0; 1 2 1]
# strength = sqrt(gx^2 + gy^2)
#
# Step 3: Small example
# 20  20 200
# 20  20 200
# 20  20 200
# gx = 720, gy = 0, strength = 720.
#
# Step 4: Python

def sobel_response(block: np.ndarray) -> tuple[float, float, float]:
    """Return gx, gy, and edge strength."""
    gx_kernel = np.array(
        [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32
    )
    gy_kernel = np.array(
        [[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32
    )

    gx = float(np.sum(block * gx_kernel))
    gy = float(np.sum(block * gy_kernel))
    strength = float(np.sqrt(gx * gx + gy * gy))
    return gx, gy, strength


problem_5_input = np.array(
    [[20, 20, 200], [20, 20, 200], [20, 20, 200]], dtype=np.float32
)
gx, gy, strength = sobel_response(problem_5_input)
assert gx == 720.0 and gy == 0.0
assert strength == 720.0
print("Problem 5 passed")


# ===========================================================================
# Final verification
# ===========================================================================
print("All Week 02 problems passed.")
