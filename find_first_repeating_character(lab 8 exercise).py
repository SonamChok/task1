def find_first_repeating_character(s):
    char_count = {}  # Dictionary to store the count of each character
    for char in s:
        if char in char_count:
            # If the character is encountered for the second time, print its memory address and return it
            print(f"First repeating character: {char}, Memory Address: {id(char)}")
            return char
        else:
            # Increment the count of the character in the dictionary
            char_count[char] = 1
    # If no repeating character is found, return None
    return None

# Example usage:
s = "abcdefgabc"
result = find_first_repeating_character(s)
if result is None:
    print("No repeating character found.")
