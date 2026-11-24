from pathlib import Path
from cryptography.exceptions import InvalidTag
from test_cipher import decrypt_vigenere, encrypt_vigenere
from test_aes import decrypt_message, encrypt_message


def encrypt_file_aes(in_path: str, out_path: str, passphrase: str):
    data = Path(in_path).read_bytes()
    if len(data) > 5 * 1024 * 1024:
        raise ValueError("Please pick a file smaller than 5 MB.")
    token = encrypt_message(data.decode("utf-8"), passphrase)
    Path(out_path).write_text(token, encoding="utf-8")


def decrypt_file_aes(in_path: str, out_path: str, passphrase: str):
    token = Path(in_path).read_text(encoding="utf-8")
    plain_text = decrypt_message(token, passphrase)
    Path(out_path).write_bytes(plain_text.encode("utf-8"))


while True:
    print("\n--- Encryption & Decryption Toolkit ---")
    print("1. Encrypt / Decrypt Text (Vigenere - Classical)")
    print("2. Encrypt / Decrypt Text (AES - Modern + Passphrase)")
    print("3. Encrypt / Decrypt Small Text File (AES + Passphrase)")
    print("4. Exit")

    choice = input("Select (1-4): ").strip()
    if choice == "4":
        break

    mode = input("Type 'e' to Encrypt or 'd' to Decrypt: ").strip().lower()

    try:
        if choice == "1":
            msg = input("Enter text: ")
            key = input("Enter letter key (e.g. KEY): ")
            out = encrypt_vigenere(msg, key) if mode == "e" else decrypt_vigenere(msg, key)
            print("Result:", out)

        elif choice == "2":
            msg = input("Enter text: ")
            pwd = input("Enter passphrase: ")
            out = encrypt_message(msg, pwd) if mode == "e" else decrypt_message(msg, pwd)
            print("Result:", out)

        elif choice == "3":
            src = input("Input file path (e.g. sample.txt): ").strip()
            dst = input("Output file path (e.g. secret.txt): ").strip()
            pwd = input("Enter passphrase: ")
            if mode == "e":
                encrypt_file_aes(src, dst, pwd)
                print("File encrypted to:", dst)
            else:
                decrypt_file_aes(src, dst, pwd)
                print("File decrypted to:", dst)
        else:
            print("Invalid option.")
    except InvalidTag:
        print("Wrong passphrase or file was modified!")
    except Exception as e:
        print("Error:", e)