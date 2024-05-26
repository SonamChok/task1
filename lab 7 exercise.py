def reverse_string(s):
    # Base case: if the string is empty or contains only one character, return the string as it is
    if len(s) <= 1:
        return s
    # Recursive case: separate the first character from the remaining characters
    first_char = s[0]
    remaining_chars = s[1:]
    # Recursively call reverse_string with the remaining characters
    reversed_remaining = reverse_string(remaining_chars)
    # Append the first character to the end of the reversed string
    return reversed_remaining + first_char

# Examples
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string(""))  # Output: ""