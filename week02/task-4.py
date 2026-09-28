import numpy as np

# Task 4
# Step 1: Inputs and output
# Input: an array and old and new value ranges.
# Output: the values mapped into the new range.
#
# Step 2: Rule
# new = (value - old_min) / (old_max - old_min)
#        * (new_max - new_min) + new_min
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
    if in_max == in_min:
        raise ValueError("in_max and in_min must be different.")

    image_float = image.astype(np.float32)
    stretched = (image_float - in_min) / (in_max - in_min)
    stretched = stretched * (out_max - out_min) + out_min

    return np.clip(stretched, out_min, out_max)


problem_4_input = np.array([50, 100, 150], dtype=np.float32)
expected = np.array([0.0, 127.5, 255.0], dtype=np.float32)

np.testing.assert_allclose(
    contrast_stretch(problem_4_input, 50, 150),
    expected
)

print("Contrast-stretched values:", contrast_stretch(problem_4_input, 50, 150))
print("Task 4 passed.")
