from Crypto.Cipher import AES

def decrypt(ciphertext_filename, key_filename):
    # Read the ciphertext file
    with open(ciphertext_filename, 'rb') as f:
        iv = f.read(16)  # Read the initialization vector (IV) of 16 bytes
        tag = f.read(16)  # Read the authentication tag of 16 bytes
        ciphertext = f.read()  # Read the encrypted ciphertext

    # Read the key from the key file
    with open(key_filename, 'rb') as key_file:
        key = key_file.read()

    # Create an AES cipher object with the provided key, IV, and mode of operation
    cipher = AES.new(key, AES.MODE_EAX, iv)

    # Decrypt the ciphertext and verify its authenticity using the provided tag
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext

# Set the filenames for the key and ciphertext files
key_filename = 'key.txt'
ciphertext_filename = 'output.txt'

# Call the decrypt function with the filenames and get the decrypted text
decrypted_text = decrypt(ciphertext_filename, key_filename)

# Print the decrypted text
print("Decrypted text:", decrypted_text.decode())