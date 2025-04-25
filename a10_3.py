import numpy as np

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n*n + 1):
        magic_square[i, j] = num
        i2, j2 = (i - 1) % n, (j + 1) % n
        if magic_square[i2, j2]:
            i = (i + 1) % n
        else:
            i, j = i2, j2
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n*n + 1).reshape(n, n)
    mask = np.ones((n, n), dtype=bool)
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                mask[i, j] = False
    magic_square[~mask] = (n*n + 1) - magic_square[~mask]
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)

    # Offsets
    add = [0, 2, 3, 1]
    for i in range(4):
        r_offset = (i // 2) * half_n
        c_offset = (i % 2) * half_n
        for r in range(half_n):
            for c in range(half_n):
                magic_square[r + r_offset, c + c_offset] = \
                    sub_square[r, c] + add[i] * half_n * half_n

    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(n):
            if j < k or j >= n - k or (j == k and i == k):
                if j % n != half_n:
                    if j < half_n:
                        magic_square[i, j], magic_square[i + half_n, j] = \
                            magic_square[i + half_n, j], magic_square[i, j]
    return magic_square

# Generate and print magic squares for N = 4 to 8
for N in range(4, 9):
    square = generate_magic_square(N)
    magic_constant = N * (N**2 + 1) // 2
    print(f"\nMagic Square (N={N}), Magic Constant = {magic_constant}:\n")
    print(square)
