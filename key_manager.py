import random  # Import the random module

def generate_key(method, difficulty):
    """Generates a key based on the method and difficulty level."""
    if method in {"AES", "DES", "BLOWFISH"}:
        # Generate a random key with length based on difficulty level
        return bytes([random.randint(0, 255) for _ in range(difficulty * 8)])
    elif method == "CAESAR":
        # Generate a random shift value for Caesar cipher
        return random.randint(1, 25)
    elif method == "RSA":
        # Generate an RSA key pair
        from Crypto.PublicKey import RSA
        return RSA.generate(2048)
    else:
        raise ValueError(f"Unsupported encryption method: {method}")
