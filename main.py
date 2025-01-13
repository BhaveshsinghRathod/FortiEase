from encryption import encrypt_data, view_encrypted_data, view_stats, add_encrypted_data
from decryption import decrypt_data
from key_manager import generate_key


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Encrypt Data")
        print("2. Decrypt Data")
        print("3. View All Encrypted Data")
        print("4. View Stats")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            method = input("Choose encryption method (AES/DES/Blowfish/Caesar/RSA): ").upper()
            difficulty = int(input("Choose difficulty level (1-Easy, 2-Medium, 3-Hard): "))
            use_auto_key = input("Do you want to auto-generate the key? (yes/no): ").lower()

            if use_auto_key == "yes":
                try:
                    if method == "RSA":
                        rsa_key = generate_key(method, difficulty)
                        print(f"Generated RSA Key Pair:\nPublic Key: {rsa_key.publickey().export_key().decode()}")
                        print(f"Private Key: {rsa_key.export_key().decode()}")
                        key = rsa_key
                    elif method == "CAESAR":
                        key = generate_key(method, difficulty)
                        print(f"Generated Caesar Cipher Shift: {key}")
                    else:
                        key = generate_key(method, difficulty)
                        print(f"Auto-generated Key: {key.hex() if isinstance(key, bytes) else key}")
                except ValueError as ve:
                    print(f"Error: {ve}")
                    continue
            else:
                key = input("Enter a key: ").encode() if method != "CAESAR" else int(input("Enter a shift value: "))

            data = input("Enter the data to encrypt: ")

            try:
                data_id, ciphertext, additional_params = encrypt_data(method, data, key, difficulty)
                print(f"Data Encrypted Successfully!")
                print(f"Data ID: {data_id}")
                print(f"Encrypted Data: {ciphertext}")
                add_encrypted_data(data_id, data, ciphertext, method, key, additional_params)
            except Exception as e:
                print(f"Error during encryption: {e}")

        elif choice == "2":
            data_id = input("Enter the ID of the encrypted data to decrypt: ")
            try:
                plaintext = decrypt_data(data_id)
                print(f"Decrypted Data: {plaintext}")
            except Exception as e:
                print(f"Error during decryption: {e}")

        elif choice == "3":
            try:
                encrypted_data = view_encrypted_data()
                print("\nEncrypted Data List:")
                for idx, data in enumerate(encrypted_data, 1):
                    print(f"{idx}. ID: {data['id']} | Method: {data['method']} | Ciphertext: {data['ciphertext']}")
            except Exception as e:
                print(f"Error retrieving data: {e}")

        elif choice == "4":
            try:
                stats = view_stats()
                print("\nEncryption Stats:")
                print(f"Total Encrypted Items: {stats['total_items']}")
                print(f"Total Data Size: {stats['total_size']} bytes")
            except Exception as e:
                print(f"Error retrieving stats: {e}")

        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
