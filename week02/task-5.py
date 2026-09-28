import numpy as np

# Task 5
# Step 1: Inputs and output
# Input: a 3 x 3 grayscale block.
# Output: gx, gy, and edge strength.
#
# Step 2: Rule
# Gx = [-1  0  1; -2  0  2; -1  0  1]
# Gy = [-1 -2 -1;  0  0  0;  1  2  1]
# strength = sqrt(gx * gx + gy * gy)
#
# Step 3: Small example
# 20 20 200
# 20 20 200
# 20 20 200
# gx = 720, gy = 0, so strength = 720.
#
# Step 4: Python

def sobel_response(block: np.ndarray) -> tuple[float, float, float]:
    gx_kernel = np.array(
        [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],
        dtype=np.float32
    )
    gy_kernel = np.array(
        [[-1, -2, -1], [0, 0, 0], [1, 2, 1]],
        dtype=np.float32
    )

    gx = float(np.sum(block * gx_kernel))
    gy = float(np.sum(block * gy_kernel))
    strength = float(np.sqrt(gx * gx + gy * gy))

    return gx, gy, strength


problem_5_input = np.array(
    [[20, 20, 200], [20, 20, 200], [20, 20, 200]],
    dtype=np.float32
)

gx, gy, strength = sobel_response(problem_5_input)

assert gx == 720.0
assert gy == 0.0
assert strength == 720.0

print("gx:", gx)
print("gy:", gy)
print("Edge strength:", strength)
print("Task 5 passed.")
