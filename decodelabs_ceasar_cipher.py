def encrypt(text, shift):
    """
    Encrypts text using a Caesar cipher with the given shift key.
    Only shifts letters A-Z and a-z. Leaves spaces, numbers, and
    punctuation unchanged (edge case handling).
    """
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # spaces, numbers, punctuation stay the same
    return result


def decrypt(text, shift):
    """
    Decrypts text that was encrypted with the Caesar cipher above,
    using the same shift key.
    """
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Encryption & Decryption ===")

    message = input("Enter the text to encrypt: ")

    while True:
        try:
            shift = int(input("Enter a shift key (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a valid whole number.")

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\n--- Result ---")
    print(f"Original Text : {message}")
    print(f"Shift Key     : {shift}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    main()
