import numpy as np

def compute_parity(mat):
    # Returns (row_parity, col_parity) for even parity
    return np.sum(mat, axis=1) % 2, np.sum(mat, axis=0) % 2
# Create a 4x4 data matrix
data = np.array([
[1, 0, 1, 1],
[0, 1, 0, 0],
[1, 1, 1, 0],
[0, 0, 1, 1]
])
print("Original Data:\n", data)
# Compute original parity bits
row_par, col_par = compute_parity(data)
print("Row Parity:", row_par)
print("Column Parity:", col_par)
# Introduce an error by flipping the bit at row 2, column 1 (0-indexed)
data_err = data.copy()
data_err[2, 1] = 1 - data_err[2, 1]
print("\nData with error at (2, 1):\n", data_err)
# Recompute parity bits after error
new_row_par, new_col_par = compute_parity(data_err)
print("New Row Parity:", new_row_par)
print("New Column Parity:", new_col_par)
# Detect and correct the error
err_row = np.where(new_row_par != row_par)[0]
err_col = np.where(new_col_par != col_par)[0]
if err_row.size == 1 and err_col.size == 1:
    error_location = (err_row[0], err_col[0])
    print("\nError detected at:", error_location)
    # Correct the error by flipping the bit back
    data_err[error_location] = 1 - data_err[error_location]
    print("Corrected Data:\n", data_err)
else:
    print("No single-bit error detected or multiple error")