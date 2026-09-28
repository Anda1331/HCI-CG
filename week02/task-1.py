import numpy as np

# Task 1
# Step 1: Inputs and output
# Input: a grayscale image and a threshold. Output: an image containing only 0 and 255.
#
# Step 2: Rule
# If pixel >= threshold, output 255; otherwise output 0.
#
# Step 3: Small example
# Input:
# 20 128 200
# 100 150 250
# With threshold 128:
# 0 255 255
# 0 255 255
#
# Step 4: Python

def threshold_image(image: np.ndarray, threshold: int) -> np.ndarray:
    return np.where(image >= threshold, 255, 0).astype(np.uint8)


problem_1_input = np.array([[20, 128, 200], [100, 150, 250]], dtype=np.uint8)
problem_1_expected = np.array([[0, 255, 255], [0, 255, 255]], dtype=np.uint8)

np.testing.assert_array_equal(
    threshold_image(problem_1_input, 128),
    problem_1_expected
)

print(threshold_image(problem_1_input, 128))
print("Task 1 passed.")
