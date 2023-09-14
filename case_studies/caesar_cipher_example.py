"""The Caesar cipher is one of the simplest and oldest encryption techniques in the history of cryptography. It is a
type of substitution cipher, where each letter in the plaintext (the message you want to encrypt) is replaced by a
letter found by moving a fixed number of positions down or up the alphabet. This fixed number of positions is called
the "shift" or "key."

Here's how the Caesar cipher works:

1. **Key/Shift**: You select a fixed integer value, known as the "shift" or "key." This value determines how many
positions each letter in the plaintext should be shifted in the alphabet.

2. **Encryption**: For each letter in the plaintext, you replace it with the letter that is shifted by the specified
key value. Letters wrap around the alphabet if the shift goes beyond 'Z' (for uppercase) or 'z' (for lowercase).

3. **Decryption**: To decrypt the message, you reverse the process by shifting each letter in the ciphertext back by
the same key value.

Here's a simple example with a shift of 3:

- Original: "HELLO"
- Encrypted: "KHOOR"

In this case, each letter in "HELLO" is shifted three positions to the right in the alphabet, resulting in "KHOOR."

The Caesar cipher is a basic and easily breakable encryption method, as there are only 25 possible keys (since a
shift of 0 or 26 is equivalent to no encryption, and a shift of 1 is equivalent to a shift of 25 in the opposite
direction). Nevertheless, it's a valuable tool for understanding the concept of encryption and cryptography. More
secure modern encryption methods use complex algorithms and much larger keys to ensure security.
"""


def caesar_cipher(text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                index = (alphabet.index(char) + shift) % 26
                shifted_char = alphabet[index]
            else:
                char = char.upper()  # Convert to uppercase for indexing
                index = (alphabet.index(char) + shift) % 26
                shifted_char = alphabet[index].lower()  # Convert back to lowercase
        else:
            shifted_char = char  # If it's not a letter, keep it unchanged
        result += shifted_char

    return result


# Example usage
plaintext = "Hello, World!"
shift_amount = 3
encrypted_text = caesar_cipher(plaintext, shift_amount)
print("Original:   ", plaintext)
print("Encrypted:  ", encrypted_text)
