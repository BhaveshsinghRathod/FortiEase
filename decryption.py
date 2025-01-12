from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES, DES, Blowfish


def decrypt_data(method, ciphertext, key, additional_params):
    if method == 1:  # AES
        cipher = AES.new(key, AES.MODE_CFB, iv=additional_params)
        return cipher.decrypt(ciphertext).decode()
    elif method == 2:  # DES
        cipher = DES.new(key, DES.MODE_CFB, iv=additional_params)
        return cipher.decrypt(ciphertext).decode()
    elif method == 3:  # RSA
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(ciphertext).decode()
    elif method == 4:  # Caesar Cipher
        shift = additional_params
        decrypted = ''.join(chr((ord(char) - shift - 32) % 95 + 32) for char in ciphertext)
        return decrypted
    elif method == 5:  # Blowfish
        cipher = Blowfish.new(key, Blowfish.MODE_CFB, iv=additional_params)
        return cipher.decrypt(ciphertext).decode()
    else:
        raise ValueError("Invalid decryption method selected.")
