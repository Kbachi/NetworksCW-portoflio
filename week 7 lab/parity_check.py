# Parity Check - Error Detection
import random

def compute_even_parity(data):
    return sum(data) % 2

def check_parity(data):
    return sum(data) % 2 == 0

def simulate_parity_error(data, error_index):
    data_with_error = data.copy()
    data_with_error[error_index] = 1 - data_with_error[error_index]
    return data_with_error

# Example Data
data = [1, 0, 1, 0, 1, 1, 0, 0]
parity_bit = compute_even_parity(data)
transmitted_data = data + [parity_bit]

print("Original Data:", data)
print("Computed Parity Bit (Even):", parity_bit)
print("Transmitted Data (Data + Parity):", transmitted_data)

# Simulate Error Injection
error_index = random.randint(0, len(transmitted_data) - 1)
data_with_error = simulate_parity_error(transmitted_data, error_index)
print("\nData with Error Introduced at index", error_index, ":", data_with_error)

# Parity Check
if check_parity(data_with_error):
    print("\nNo error detected (Parity Check Passed)")
else:
    print("\nError detected (Parity Check Failed)")
