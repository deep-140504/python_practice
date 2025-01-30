import numpy as np

# Create a 2D NumPy array
arr = np.array([  [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

# Create index arrays for rows and columns
row_indices = np.array([0, 1, 2])  # Select rows 0, 1, 2
col_indices = np.array([1, 2, 3])     # Select columns 1 and 2

# Use slicing and index arrays to select a rectangular subarray
# print(arr[row_indices, col_indices])
print(row_indices[:, None])
print(col_indices[:, None])
print(arr[row_indices[:, None]])
print('-'*50)
subarray = arr[row_indices[:, None], col_indices[:, None]]

print("Original array:")
print(arr)

print("\nSelected rectangular subarray:")
print(subarray)





print('-'*100)

tarr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

diag_matrix = np.zeros_like(tarr)  # Create a zero matrix of the same shape as arr
diag_matrix[np.arange(tarr.shape[0]), np.arange(tarr.shape[1])] = tarr.diagonal()

print(diag_matrix)
