def decode_ways(encoded):
    def backtrack(index, path):
        if index == len(encoded):
            results.append(''.join(path))
            return
        
        # Single digit mapping (1-9)
        if 1 <= int(encoded[index]) <= 9:
            backtrack(index + 1, path + [chr(int(encoded[index]) + 64)])
        
        # Two digits mapping (10-26)
        if index + 1 < len(encoded) and 10 <= int(encoded[index:index + 2]) <= 26:
            backtrack(index + 2, path + [chr(int(encoded[index:index + 2]) + 64)])

    results = []
    backtrack(0, [])
    return results

# Take input from user
encoded_message = input("Enter the encoded message: ")
decoded_messages = decode_ways(encoded_message)
print("Possible decodings:")
for i, msg in enumerate(decoded_messages, 1):
    print(f"{i}. {msg}")
