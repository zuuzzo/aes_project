import os
import binascii

# Generate a random key
key = os.urandom(16)

# Convert the key to a string of hexadecimal digits
hex_key = binascii.hexlify(key).decode()

# Save the key to a file named key.txt
with open('key.txt', 'w') as f:
    f.write(hex_key)

# Print a message indicating that the key has been saved
print('Key saved to key.txt')
