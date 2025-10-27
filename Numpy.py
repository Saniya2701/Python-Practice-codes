
import numpy as np


arr = np.array([10, 20, 30, 40, 50])
print("1. Original Array:", arr)

zeros_arr = np.zeros((2, 3))
print("\n2. Zeros Array:\n", zeros_arr)


ones_arr = np.ones((2, 3))
print("\n3. Ones Array:\n", ones_arr)


range_arr = np.arange(1, 11, 2)
print("\n4. Range Array:", range_arr)


reshaped = np.arange(6).reshape(2, 3)
print("\n5. Reshaped Array (2x3):\n", reshaped)


mean_value = np.mean(arr)
print("\n6. Mean of Array:", mean_value)


std_value = np.std(arr)
print("\n7. Standard Deviation:", std_value)


sum_arr = arr + 5
print("\n8. Element-wise Addition:", sum_arr)


print("\n9. Max:", np.max(arr))
print("\n10. Min:", np.min(arr))

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
result = np.dot(mat1, mat2)
print("\n11. Matrix Multiplication Result:\n", result)
