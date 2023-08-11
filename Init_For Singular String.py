import numpy as np

def binary_pascal(n):
    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        # Generate the next row
        for j in range(len(last_row)-1):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)
        triangle.append(row)

    # Convert to binary and flatten
    binary_triangle = []
    for row in triangle:
        binary_row = [bin(x)[2:] for x in row]  # Remove '0b' prefix
        binary_triangle.extend(binary_row)

    # Determine if we need to add a zero in the middle
    if len(binary_triangle) % 2 == 0:
        binary_triangle.insert(len(binary_triangle) // 2, '0')

    # Convert to numpy array
    binary_triangle = np.array([int(b) for b in binary_triangle])

    return binary_triangle


# Set print options
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# Example usage:
print(binary_pascal(4))
