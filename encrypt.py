from Crypto.Cipher import AES
import os

def encrypt(message, key_filename):
    with open(key_filename, 'rb') as key_file:
        key = key_file.read()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_EAX, iv)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    with open('output.txt', 'wb') as output_file:
        [output_file.write(x) for x in (iv, tag, ciphertext)]

    return ciphertext

text = input("Enter text to encrypt: ")
key_filename = "key.txt"
encrypted_text = encrypt(text.encode(), key_filename)
print("Encrypted text:", encrypted_text.hex())