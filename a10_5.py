import numpy as np

# Sample NumPy array of strings
arr = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])

# Set the desired length
width = 15
pad_char = '_'

# Centered
centered = np.array([s.center(width, pad_char) for s in arr])
# Left-justified
left_justified = np.array([s.ljust(width, pad_char) for s in arr])
# Right-justified
right_justified = np.array([s.rjust(width, pad_char) for s in arr])

# Display results
print("Original Array:\n", arr)
print("\nCentered:\n", centered)
print("\nLeft-Justified:\n", left_justified)
print("\nRight-Justified:\n", right_justified)
