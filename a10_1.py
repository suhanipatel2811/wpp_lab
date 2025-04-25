import matplotlib
import matplotlib.pyplot as plt
import numpy as np
def is_safe(positions, row, col):
    for r in range(row):
        c = positions[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n=8):
    positions = np.full(n, -1)
    solutions = []

    def place_queen(row):
        if row == n:
            solutions.append(np.copy(positions))
            return
        for col in range(n):
            if is_safe(positions, row, col):
                positions[row] = col
                place_queen(row + 1)
                positions[row] = -1

    place_queen(0)
    return solutions

def draw_board(solution, ax):
    n = len(solution)
    # Draw the checkerboard
    for row in range(n):
        for col in range(n):
            color = 'cornsilk' if (row + col) % 2 == 0 else 'lightslategrey'
            ax.add_patch(plt.Rectangle((col, n - row - 1), 1, 1, color=color))
    
    # Draw the queens
    for row, col in enumerate(solution):
        ax.text(col + 0.5, n - row - 1 + 0.5, '♕', fontsize=24, ha='center', va='center', color='black')

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

# Solve and visualize first 4 solutions
solutions = solve_n_queens()
print(f"Total solutions found: {len(solutions)}")

# Plot first 4 solutions
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i in range(4):
    draw_board(solutions[i], axes[i])
    axes[i].set_title(f"Solution {i + 1}")

plt.tight_layout()
plt.show()
