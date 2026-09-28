import numpy as np

# Task 3
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
# Sum = 190, so 190 / 9 = 21.11..., rounded to 21.
#
# Step 4: Python

def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    return int(round(float(np.sum(neighborhood)) / 9))


problem_3_input = np.array(
    [[10, 20, 10], [30, 50, 30], [10, 20, 10]],
    dtype=np.uint8
)

assert mean_filter_3x3(problem_3_input) == 21

print("Average:", mean_filter_3x3(problem_3_input))
print("Task 3 passed.")
