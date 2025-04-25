import numpy as np
import matplotlib.pyplot as plt
import random

def is_valid(solution):
    # Check diagonal conflicts
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            if abs(solution[i] - solution[j]) == abs(i - j):
                return False
    return True

def find_random_solution():
    while True:
        solution = list(np.random.permutation(8))
        if is_valid(solution):
            return solution

def draw_board(solution):
    fig, ax = plt.subplots()
    n = len(solution)
    for row in range(n):
        for col in range(n):
            color = 'cornsilk' if (row + col) % 2 == 0 else 'gray'
            ax.add_patch(plt.Rectangle((col, n - row - 1), 1, 1, color=color))
    for row, col in enumerate(solution):
        ax.text(col + 0.5, n - row - 1 + 0.5, '♕', fontsize=24, ha='center', va='center', color='black')
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.title("Random Valid 8 Queens Placement")
    plt.show()

# Find and display a random valid solution
solution = find_random_solution()
print("Random valid 8-queen placement (row: column):")
for i, col in enumerate(solution):
    print(f"Row {i}: Column {col}")
draw_board(solution)
