# Crypto Toolkit (InfozaTech Cybersecurity Internship — Task 4)

A command-line encryption and decryption toolkit in Python covering classical and modern cryptography.

## Features
- **Vigenère Cipher (`test_cipher.py`):** Classical alphabetic substitution encryption and decryption using a letter key.
- **AES-256-GCM + PBKDF2 (`test_aes.py`):** Modern authenticated encryption using AES-256-GCM with passphrase-based key derivation (`PBKDF2-HMAC-SHA256`), random salt, and random nonce.
- **Interactive CLI (`app.py`):** Menu-driven tool supporting:
  1. Vigenère text encryption / decryption
  2. AES text encryption / decryption
  3. AES small text file encryption / decryption
- **Classical vs. Modern Comparison (`comparison.md`):** Comparison of Vigenère and AES-256 across mechanics, security strength, file handling, and practical use.

## Setup & Usage
Install the required dependency:

```bash
pip install cryptography
