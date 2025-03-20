import random

# compute 2D parity
def compute_parity(matrix):
    row_parity = [sum(row) % 2 for row in matrix]
    col_parity = [sum(col) % 2 for col in zip(*matrix)]
    return row_parity, col_parity

# Example Data Matrix
data = [
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
]

print("Original Data:")
for row in data:
    print(row)

# Compute original parity bits
row_parity, col_parity = compute_parity(data)
print("Row Parity:", row_parity)
print("Column Parity:", col_parity)

# Introduce an error by flipping a bit
error_row, error_col = random.randint(0, 3), random.randint(0, 3)
data_with_error = [row[:] for row in data]  # Deep copy

data_with_error[error_row][error_col] = 1 - data_with_error[error_row][error_col]
print("\nData with error at", (error_row, error_col), ":")
for row in data_with_error:
    print(row)

# Recompute parity after error
new_row_parity, new_col_parity = compute_parity(data_with_error)
print("New Row Parity:", new_row_parity)
print("New Column Parity:", new_col_parity)

# correct the error
err_row = [i for i in range(len(row_parity)) if new_row_parity[i] != row_parity[i]]
err_col = [j for j in range(len(col_parity)) if new_col_parity[j] != col_parity[j]]

if len(err_row) == 1 and len(err_col) == 1:
    detected_error = (err_row[0], err_col[0])
    print("\nError detected at:", detected_error)
    # Correct the error
    data_with_error[detected_error[0]][detected_error[1]] = 1 - data_with_error[detected_error[0]][detected_error[1]]
    print("Corrected Data:")
    for row in data_with_error:
        print(row)
else:
    print("No single-bit error detected or multiple errors occurred.")
