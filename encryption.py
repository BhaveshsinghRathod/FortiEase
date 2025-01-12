from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES, DES, Blowfish


def encrypt_data(method, data, key, difficulty):
    if method == 1:  # AES
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(data.encode())
        return ciphertext, cipher.iv
    elif method == 2:  # DES
        cipher = DES.new(key, DES.MODE_CFB)
        ciphertext = cipher.encrypt(data.encode())
        return ciphertext, cipher.iv
    elif method == 3:  # RSA
        cipher = PKCS1_OAEP.new(key.publickey())
        ciphertext = cipher.encrypt(data.encode())
        return ciphertext, None
    elif method == 4:  # Caesar Cipher
        shift = difficulty * 3
        encrypted = ''.join(chr((ord(char) + shift - 32) % 95 + 32) for char in data)
        return encrypted, shift
    elif method == 5:  # Blowfish
        cipher = Blowfish.new(key, Blowfish.MODE_CFB)
        ciphertext = cipher.encrypt(data.encode())
        return ciphertext, cipher.iv
    else:
        raise ValueError("Invalid encryption method selected.")
