import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def make_key_from_passphrase(passphrase: str, salt: bytes) -> bytes:
    # Turns a human passphrase into a strong 32-byte (256-bit) key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
    )
    return kdf.derive(passphrase.encode("utf-8"))


def encrypt_message(message: str, passphrase: str) -> str:
    salt = os.urandom(16)   # Random salt so same password gives different output
    nonce = os.urandom(12)  # Random nonce required for AES-GCM
    key = make_key_from_passphrase(passphrase, salt)

    ciphertext = AESGCM(key).encrypt(nonce, message.encode("utf-8"), None)
    # Combine salt + nonce + ciphertext and encode as readable text
    combined = salt + nonce + ciphertext
    return base64.b64encode(combined).decode("utf-8")


def decrypt_message(token: str, passphrase: str) -> str:
    raw = base64.b64decode(token.encode("utf-8"))
    salt = raw[:16]
    nonce = raw[16:28]
    ciphertext = raw[28:]

    key = make_key_from_passphrase(passphrase, salt)
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")


secret_token = encrypt_message("My secret bank PIN is 4829", "my-strong-passphrase")
print("AES Encrypted:", secret_token)
print("AES Decrypted:", decrypt_message(secret_token, "my-strong-passphrase"))