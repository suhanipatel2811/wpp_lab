import pandas as pd

# Given Pandas Series
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert all string values to uppercase
s_upper = s.str.upper()

# Convert all string values to lowercase
s_lower = s.str.lower()

# Find the length of each string
s_length = s.str.len()

# Display the results
print("Original Series:\n", s)
print("\nUppercase:\n", s_upper)
print("\nLowercase:\n", s_lower)
print("\nLength of each string:\n", s_length)
