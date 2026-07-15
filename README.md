Caesar Cipher Encryption & Decryption

DecodeLabs Cyber Security Internship — Project 2

A Python program that encrypts and decrypts text using the Caesar cipher — a classic substitution cipher that shifts each letter by a fixed number of positions in the alphabet.

Goal

Implement a simple, reversible encryption and decryption technique to understand the fundamentals of data confidentiality.

Key Requirements


Encrypt user text using a basic logic (Caesar cipher)
Decrypt the encrypted text
Display both encrypted and decrypted output


Key Skills Used


Encryption concepts
Logic building
Data protection basics


How It Works

Each letter in the text is shifted forward by a chosen shift key (n) using the formula:

Encryption: E(x) = (x + n) % 26
Decryption: D(x) = (x - n) % 26

Where x is the letter's position in the alphabet (A=0, B=1, ... Z=25).


Uppercase and lowercase letters are shifted independently, preserving their case
Spaces, numbers, and punctuation are left unchanged (not part of the cipher alphabet)
The alphabet wraps around — e.g. with a shift of 3, X becomes A
This is a symmetric cipher: the same key that encrypts also decrypts (by shifting in reverse)


How to Run

bashpython caesar_cipher.py

You'll be prompted to enter the text you want to encrypt and a shift key. The program then displays the original text, the encrypted text, and the decrypted text (to confirm it matches the original).

Example

=== Caesar Cipher Encryption & Decryption ===
Enter the text to encrypt: Hello, World!
Enter a shift key (e.g. 3): 5

--- Result ---
Original Text : Hello, World!
Shift Key     : 5
Encrypted Text: Mjqqt, Btwqi!
Decrypted Text: Hello, World!

Known Limitations

The Caesar cipher is a learning tool, not a secure encryption method:


Only 25 possible shift keys — trivial to brute-force
Vulnerable to frequency analysis, since letter patterns are preserved in the ciphertext


Modern systems use algorithms like AES-256, which rely on much larger keys and more complex transformations (confusion + diffusion, XOR operations) rather than a simple shift.

Requirements


Python 3.x (uses only built-in functions ord() and chr() — no installation needed)
