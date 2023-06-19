from Crypto.Cipher import AES
import os

def encrypt(message, key_filename):
    # Read the key from the key file
    with open(key_filename, 'rb') as key_file:
        key = key_file.read()

    # Generate a random initialization vector (IV) of 16 bytes
    iv = os.urandom(16)

    # Create an AES cipher object with the provided key, IV, and mode of operation
    cipher = AES.new(key, AES.MODE_EAX, iv)

    # Encrypt the message and obtain the ciphertext and authentication tag
    ciphertext, tag = cipher.encrypt_and_digest(message)

    # Write the IV, tag, and ciphertext to the output file
    with open('output.txt', 'wb') as output_file:
        [output_file.write(x) for x in (iv, tag, ciphertext)]

    return ciphertext

# Get the text to encrypt from user input
text = input("Enter text to encrypt: ")

# Set the filename for the key file
key_filename = "key.txt"

# Call the encrypt function with the text and key filename, and get the encrypted text
encrypted_text = encrypt(text.encode(), key_filename)

# Print the encrypted text in hexadecimal format
print("Encrypted text:", encrypted_text.hex())
