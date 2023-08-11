import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

def binary_pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for j in range(len(last_row)-1):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)
        triangle.append(row)

    binary_triangle = []
    max_width = 0
    for row in triangle:
        binary_row = [list(bin(x)[2:]) for x in row]
        binary_row = [digit for number in binary_row for digit in number]
        if len(binary_row) % 2 == 0:
            binary_row.insert(len(binary_row) // 2, '0')
        max_width = max(max_width, len(binary_row))
        binary_triangle.append(binary_row)

    for i, row in enumerate(binary_triangle):
        padding = ['0'] * ((max_width - len(row)) // 2)
        binary_row = padding + row + padding
        if len(binary_row) < max_width:
            binary_row.append('0')
        binary_triangle[i] = binary_row

    # Padding rows to create square matrix
    pad_rows = max_width - len(binary_triangle)
    binary_triangle = [['0']*max_width]*pad_rows + binary_triangle + [['0']*max_width]*pad_rows

    binary_triangle = np.array([[int(b) for b in row] for row in binary_triangle])

    return binary_triangle


np.set_printoptions(threshold=np.inf, linewidth=np.inf)

def array_to_bin_matrix(bin_array):
    # Ensure that bin_array is 2D
    if bin_array.ndim == 1:
        bin_array = bin_array[np.newaxis, :]
    return bin_array.tolist()

def update_matrix(matrix):
    matrix = np.array(matrix)  # Convert the matrix to a numpy array
    updated_matrix = matrix.copy()
    height, width = matrix.shape
    # loop over each cell in the matrix
    for i in range(height):
        for j in range(width):
            # check the number of black cells surrounding the current cell
            n_black = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x, y) != (i, j) and x >= 0 and y >= 0 and x < height and y < width:
                        if matrix[x, y] == 1:
                            n_black += 1

            # invert the cell color if a white cell borders 2 black cells
            if matrix[i, j] == 0 and n_black == 2:
                updated_matrix[i, j] = 1
            elif matrix[i, j] == 1 and n_black % 2 == 1:
                # turn two diagonal black cells to white
                if i > 0 and j > 0 and matrix[i - 1, j - 1] == 1:
                    updated_matrix[i - 1, j - 1] = 0
                if i > 0 and j < width - 1 and matrix[i - 1, j + 1] == 1:
                    updated_matrix[i - 1, j + 1] = 0
                if i < height - 1 and j > 0 and matrix[i + 1, j - 1] == 1:
                    updated_matrix[i + 1, j - 1] = 0
                if i < height - 1 and j < width - 1 and matrix[i + 1, j + 1] == 1:
                    updated_matrix[i + 1, j + 1] = 0


    return updated_matrix.tolist()  # Convert the numpy array back into a list



fig, ax = plt.subplots()

initial_state = array_to_bin_matrix(binary_pascal(32))

def animate(i):
    global initial_state
    initial_state = update_matrix(initial_state)
    ax.imshow(initial_state, cmap='binary')

ani = animation.FuncAnimation(fig, animate, frames=63, interval=20)

# Save the animation as a GIF
#ani.save('Pascal_Singular.gif', writer=PillowWriter(fps=1))


plt.show()
