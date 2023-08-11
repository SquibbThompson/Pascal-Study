import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# convert binary string to matrix
def string_to_bin_matrix(bin_string):
    return [[int(bit) for bit in line] for line in bin_string.split('\n') if line]




binary_string = """



""".strip()

# generate initial state
initial_state = np.array(string_to_bin_matrix(binary_string))

def update_matrix(matrix):
    updated_matrix = matrix.copy()
    height, width = matrix.shape

    # loop over each cell in the matrix
    for i in range(height):
        for j in range(width):
            # check the number of black cells surrounding the current cell
            n_1 = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x, y) != (i, j) and x >= 0 and y >= 0 and x < height and y < width:
                        if matrix[x, y] == 1:
                            n_1 += 1

            # invert the cell color if a white cell borders an even number of black cells
            if matrix[i, j] == 0 and n_1 % 2 == 0 and n_1 != 0:
                updated_matrix[i, j] = 1
            elif matrix[i, j] == 1 and n_1 % 2 == 1:
                # turn two horizontal/vertical black cells to white
                if i > 0 and matrix[i - 1, j] == 1:
                    updated_matrix[i - 1, j] = 0
                if j > 0 and matrix[i, j - 1] == 1:
                    updated_matrix[i, j - 1] = 0
                if i < height - 1 and matrix[i + 1, j] == 1:
                    updated_matrix[i + 1, j] = 0
                if j < width - 1 and matrix[i, j + 1] == 1:
                    updated_matrix[i, j + 1] = 0
    return updated_matrix

# animate cellular automata evolution
def animate(i):
    global initial_state

    initial_state = update_matrix(initial_state)
    plt.imshow(initial_state, cmap='binary')

fig, ax = plt.subplots()
global ani
ani = animation.FuncAnimation(fig, animate, frames=34, interval=20)


plt.show()


