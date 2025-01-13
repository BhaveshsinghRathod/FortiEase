import hashlib
import random
import string
from key_manager import generate_key

ENCRYPTED_DATA = []  # Global list to store encrypted data
TOTAL_STATS = {"total_items": 0, "total_size": 0}


def generate_data_id():
    """Generates a unique data ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def encrypt_data(method, data, key, difficulty):
    """Encrypts the given data based on the chosen method."""
    data_id = generate_data_id()
    ciphertext = None
    additional_params = {}

    if method == "AES":
        # AES encryption logic
        ciphertext = hashlib.sha256(data.encode()).hexdigest()  # Placeholder logic
    elif method == "DES":
        # DES encryption logic
        ciphertext = hashlib.md5(data.encode()).hexdigest()  # Placeholder logic
    elif method == "BLOWFISH":
        # Blowfish encryption logic
        ciphertext = hashlib.sha1(data.encode()).hexdigest()  # Placeholder logic
    elif method == "CAESAR":
        shift = key
        ciphertext = ''.join(
            chr((ord(char) + shift - 65) % 26 + 65) if char.isupper() else char
            for char in data
        )
        additional_params["shift"] = shift
    elif method == "RSA":
        # RSA encryption logic
        ciphertext = "EncryptedWithRSA"  # Placeholder logic
        additional_params["rsa_key"] = key

    # Update stats and return
    TOTAL_STATS["total_items"] += 1
    TOTAL_STATS["total_size"] += len(ciphertext)
    return data_id, ciphertext, additional_params


def add_encrypted_data(data_id, plaintext, ciphertext, method, key, additional_params):
    """Stores encrypted data along with its metadata."""
    ENCRYPTED_DATA.append({
        "id": data_id,
        "plaintext": plaintext,
        "ciphertext": ciphertext,
        "method": method,
        "key": key,
        "additional_params": additional_params
    })


def view_encrypted_data():
    """Returns all encrypted data."""
    return ENCRYPTED_DATA


def view_stats():
    """Returns encryption statistics."""
    return TOTAL_STATS
