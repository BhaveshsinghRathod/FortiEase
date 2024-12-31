from encryption import encrypt_data
from decryption import decrypt_data
from key_manager import generate_key

def display_menu():
    print("Welcome to FortiEase!")
    print("Choose an encryption method:")
    print("1. AES (Advanced Encryption Standard)")
    print("2. DES (Data Encryption Standard)")
    print("3. RSA (Rivest-Shamir-Adleman)")
    print("4. Caesar Cipher")
    print("5. Blowfish")
    return int(input("Enter your choice (1-5): "))

def select_difficulty():
    print("\nSelect difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    return int(input("Enter your choice (1-3): "))

def main():
    method = display_menu()
    difficulty = select_difficulty()
    data = input("\nEnter the data to encrypt: ")

    # Generate a key if needed
    key = generate_key(method, difficulty)

    # Encrypt data
    ciphertext, additional_params = encrypt_data(method, data, key, difficulty)

    print("\nEncrypted data:", ciphertext)
    
    # Decrypt data
    decrypted = decrypt_data(method, ciphertext, key, additional_params)
    print("Decrypted data:", decrypted)

if __name__ == "__main__":
    main()
