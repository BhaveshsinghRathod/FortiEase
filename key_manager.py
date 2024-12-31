from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

def generate_key(method, difficulty):
    if method == 1:  # AES
        key_sizes = {1: 16, 2: 24, 3: 32}  # Easy, Medium, Hard
        return get_random_bytes(key_sizes[difficulty])
    elif method == 2:  # DES
        return get_random_bytes(8)  # DES uses an 8-byte key
    elif method == 3:  # RSA
        key_sizes = {1: 1024, 2: 2048, 3: 4096}  # Updated to meet minimum requirements
        return RSA.generate(key_sizes[difficulty])
    elif method == 5:  # Blowfish
        key_sizes = {1: 16, 2: 24, 3: 32}  # Easy, Medium, Hard
        return get_random_bytes(key_sizes[difficulty])
    else:
        return None  # Caesar Cipher does not require a key
