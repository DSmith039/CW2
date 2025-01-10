def cyclic_shift(m, shift):
    if shift < 0 or shift >= len(m):
        return m
    shift = shift % len(m)
    return m[-shift:] + m[:-shift]


def encrypt_message_interactive():
    # Step 1: Accept an encryption key containing 6 characters from user input
    key = input("Enter a 6-character encryption key: ")
    while len(key) != 6:
        print("Key must be exactly 6 characters long.")
        key = input("Enter a 6-character encryption key: ")
    print(f"Step 1: Key accepted: {key}")

    # Step 2: Accept a message m to be encrypted
    message = input("Enter the message to be encrypted: ")
    print(f"Step 2: Original message: {message}")

    # Step 3: Pad out the message with additional “a” characters until its new length is a multiple of 8
    while len(message) % 8 != 0:
        message += "a"
    print(f"Step 3: Padded message: {message}")

    # Step 4: Split the new message into list of subsequences of 8 characters
    subsequences = [message[i:i + 8] for i in range(0, len(message), 8)]
    print(f"Step 4: Subsequences: {subsequences}")

    # Step 5: Calculate shift1 from the first two characters of the key
    shift1 = (ord(key[0]) + ord(key[1])) % 8
    print(f"Step 5: Shift1 value: {shift1}")

    # Step 6: Perform a right cyclic shift of size shift1 on each subsequence
    shifted_subsequences = [cyclic_shift(subseq, shift1) for subseq in subsequences]
    print(f"Step 6: Shifted subsequences: {shifted_subsequences}")

    # Step 7: Calculate shift2 from the third and fourth characters of the key
    shift2 = (ord(key[2]) + ord(key[3])) % 3
    print(f"Step 7: Shift2 value: {shift2}")

    # Step 8: Perform a cyclic shift of size shift2 on the list of subsequences
    final_subsequences = cyclic_shift(shifted_subsequences, shift2)
    print(f"Step 8: Final shifted subsequences: {final_subsequences}")

    # Step 9: Concatenate the subsequences together to form the encrypted message
    encrypted_message = "".join(final_subsequences)
    print(f"Step 9: Encrypted message: {encrypted_message}")

    return encrypted_message


# Running the interactive encryption function
encrypted_message = encrypt_message_interactive()
print("Final Encrypted Message:", encrypted_message)
