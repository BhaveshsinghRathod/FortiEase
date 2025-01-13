from encryption import ENCRYPTED_DATA


def decrypt_data(data_id):
    """Decrypts data based on the data ID."""
    for item in ENCRYPTED_DATA:
        if item["id"] == data_id:
            # Decrypt using the relevant method
            return item["plaintext"]  # Placeholder logic
    raise ValueError("Data ID not found!")
