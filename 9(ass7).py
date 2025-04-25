import re

# Define the regular expressions for tokenization
patterns = {
    'punctuation': r'[\.,!?;:"]',  # Punctuation marks
    'dates': r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',  # Dates like 12/05/2021 or 12-05-2021
    'urls': r'(https?://[^\s]+|www\.[^\s]+)',  # URLs starting with http:// or www.
    'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',  # Email addresses
    'numbers': r'\b\d{1,3}(?:[,\.\d]*\d+)?\b',  # Numbers including decimals and commas
    'handles': r'@\w+',  # Social media handles, e.g., @username
    'hindi': r'[\u0900-\u097F]+',  # Hindi Unicode block
}

# Function to tokenize text using regular expressions
def tokenizer(text):
    tokens = []
    
    # Combine all regex patterns into one
    combined_pattern = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in patterns.items())
    
    # Find all matches
    for match in re.finditer(combined_pattern, text):
        for key, value in match.groupdict().items():
            if value:  # If the group is not None, it's a match
                tokens.append((key, value))
    
    return tokens

# Function to display the tokenized output
def display_tokens(tokens):
    for token in tokens:
        print(f"Token Type: {token[0]}, Token: {token[1]}")

# Take input from the user
text = input("Enter text to tokenize: ")

# Tokenize the input text
tokens = tokenizer(text)

# Display the tokenized output
display_tokens(tokens)
