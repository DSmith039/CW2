def cyclic_shift(m, shift):
    # If shift is negative or greater than or equal to the length of m, return m as-is
    if shift < 0 or shift >= len(m):
        return m

    # Calculate the effective shift using modulo to avoid unnecessary large shifts
    shift = shift % len(m)

    # Return the shifted message by concatenating the two parts
    return m[-shift:] + m[:-shift]


def cyclic_unshift(m, shift):
    # Calculate the effective unshift using modulo to avoid unnecessary large shifts
    unshift = (-shift) % len(m)

    # Use the cyclic_shift function with the effective unshift
    return cyclic_shift(m, unshift)


# Test with a string
print(cyclic_shift("This is a secret message", 2))  # Output: "geThis is a secret messa"

# Test with a list of numbers
print(cyclic_shift([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

# Test with a list of strings
print(cyclic_shift(["a", "b", "c", "d"], 1))  # Output: ["d", "a", "b", "c"]

# Test with a list of lists
print(cyclic_shift([[1], [2], [3], [4]], 3))  # Output: [[2], [3], [4], [1]]

# Example: Encrypt and then decrypt a message
shifted_message = cyclic_shift("This is a secret message", 2)
print(shifted_message)  # Output: "geThis is a secret messa"

original_message = cyclic_unshift(shifted_message, 2)
print(original_message)  # Output: "This is a secret message"
