def encrypt_vigenere(text, key):
    key = key.upper()
    result = ""
    i = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[i % len(key)]) - ord("A")
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
            i += 1
        else:
            result += ch
    return result


def decrypt_vigenere(cipher, key):
    key = key.upper()
    result = ""
    i = 0
    for ch in cipher:
        if ch.isalpha():
            shift = ord(key[i % len(key)]) - ord("A")
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base - shift) % 26 + base)
            i += 1
        else:
            result += ch
    return result


secret = encrypt_vigenere("Hello World", "KEY")
print("Encrypted:", secret)
print("Decrypted:", decrypt_vigenere(secret, "KEY"))